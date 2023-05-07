from torch import nn


class ClsLoss(nn.Module):

    def __init__(self, label_smoothing=0., reduction='mean'):
        super(ClsLoss, self).__init__()
        self.loss_func = nn.CrossEntropyLoss(reduction='none',
                                             label_smoothing=label_smoothing)
        self.reduction = reduction

    def forward(self, predicts, batch):
        label = batch[1]
        loss = self.loss_func(input=predicts, target=label)
        if self.reduction == 'mean':
            loss = loss.mean()
        return {'loss': loss}
