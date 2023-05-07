import copy

from .resnet import ResNet18

__all__ = ["build_backbone"]


def build_backbone(config):
    config = copy.deepcopy(config)
    support_dict = ['ResNet18']

    module_name = config.pop("name")
    assert module_name in support_dict, Exception(
        "backbone only support {}".format(support_dict))
    module_class = eval(module_name)(**config)
    return module_class
