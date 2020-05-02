"""
Custom YAML serializers that maintain their order
"""
import yaml
from django.core.serializers.pyyaml import DjangoSafeDumper


class OrderedLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node):
    loader.flatten_mapping(node)
    return dict(loader.construct_pairs(node))


OrderedLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping
)


class OrderedDumper(DjangoSafeDumper):
    pass


def _dict_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items()
    )


OrderedDumper.add_representer(dict, _dict_representer)
