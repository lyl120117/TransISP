import copy

from .optimizer import *
from .learning_rate import *

__all__ = ['build_optimizer']


def build_scheduler(config, optimizer, max_steps):
    support_dict = ["CosineAnnealing", 'MultiStep']

    config = copy.deepcopy(config)
    module_name = config.pop("name")
    assert module_name in support_dict, Exception(
        "schedule only support {}".format(support_dict))

    module_class = eval(module_name)(**config)
    return module_class(optimizer)


def build_optimizer(config, epochs, step_each_epoch, parameters):
    support_dict = ["Adam", 'SGD']

    config = copy.deepcopy(config)
    module_name = config.pop("name")
    assert module_name in support_dict, Exception(
        "optimizer only support {}".format(support_dict))
    module_class = eval(module_name)(**config)
    return module_class(parameters)
