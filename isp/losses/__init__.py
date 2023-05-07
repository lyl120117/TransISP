import copy

from .cls_loss import ClsLoss

__all__ = ['build_loss']


def build_loss(config):
    support_dict = ['ClsLoss']
    config = copy.deepcopy(config)
    module_name = config.pop('name')
    assert module_name in support_dict, Exception(
        'loss only support {}'.format(support_dict))
    module_class = eval(module_name)(**config)
    return module_class
