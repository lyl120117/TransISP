import copy

__all__ = ['build_post_process']

from .cls_postprocess import ClsPostProcess


def build_post_process(config, global_config=None):
    support_dict = ['ClsPostProcess']

    config = copy.deepcopy(config)
    module_name = config.pop('name')
    if global_config is not None:
        config.update(global_config)
    assert module_name in support_dict, Exception(
        'post process only support {}'.format(support_dict))
    module_class = eval(module_name)(**config)
    return module_class
