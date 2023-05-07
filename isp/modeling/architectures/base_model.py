from torch import nn
from isp.modeling.backbones import build_backbone
from isp.modeling.heads import build_head
from isp.modeling.necks import build_neck

__all__ = ['BaseModel']


class BaseModel(nn.Module):

    def __init__(self, config):
        """
        the module for Face Recognition.
        args:
            config (dict): the super parameters for module.
        """
        super(BaseModel, self).__init__()
        in_channels = config.get('in_channels', 3)

        # build backbone, backbone is need for del, rec and cls
        config["Backbone"]['in_channels'] = in_channels
        self.backbone = build_backbone(config["Backbone"])
        in_channels = self.backbone.out_channels

        # build neck
        # for rec, neck can be cnn,rnn or reshape(None)
        # for det, neck can be FPN, BIFPN and so on.
        # for cls, neck should be none
        if 'Neck' not in config or config['Neck'] is None:
            self.use_neck = False
        else:
            self.use_neck = True
            config['Neck']['in_channels'] = in_channels
            self.neck = build_neck(config['Neck'])
            in_channels = self.neck.out_channels

        # # build head, head is need for det, rec and cls
        config["Head"]['in_channels'] = in_channels
        self.head = build_head(config["Head"])

        self.return_all_feats = config.get("return_all_feats", False)

    def to(self, device):
        self = super(BaseModel, self).to(device)
        self.head.to(device)
        return self

    def forward(self, x, data=None):
        y = dict()

        x = self.backbone(x)
        y["backbone_out"] = x

        if self.use_neck:
            x = self.neck(x)
        y["neck_out"] = x

        x = self.head(x, targets=data)
        if isinstance(x, dict):
            y.update(x)
        else:
            y["head_out"] = x
        if self.return_all_feats:
            return y
        else:
            return x
