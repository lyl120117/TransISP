import torch
from isp.utils.utility import parse_dict
import numpy as np


class ClsPostProcess(object):
    """Convert between text-label and text-index"""

    def __init__(self, dict_path, **kwargs):
        super(ClsPostProcess, self).__init__()
        self.dicts = parse_dict(dict_path)
        self.label_list = self.dicts

    def __call__(self, preds, label=None, *args, **kwargs):
        if isinstance(preds, torch.Tensor):
            preds = preds.cpu().detach().numpy()
        if len(preds) == 2:
            preds = preds[0]
        pred_idxs = preds.argmax(axis=1)

        decode_out = [(self.dicts[idx], preds[i, idx])
                      for i, idx in enumerate(pred_idxs)]
        if label is None:
            return decode_out
        label = [(self.dicts[idx], 1.0) for idx in label]
        return decode_out, label
