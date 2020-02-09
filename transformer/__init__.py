from core.database import reference_interface, database_binding
from transformer import (
    basic_transforms
)


def get_configuration(source_topic, target_topic):
    with database_binding.DatabaseBinding("core") as binding:
        interface = reference_interface.ReferenceInterface(bind=binding.engine)
        return interface.get_subscription(source_topic, target_topic)


def transform_record(record, transform_list):
    output = {
        "_record": record,
    }
    for transform in transform_list:
        method = _transform_map[transform["method"]]
        method(record, transform, output)

    return output


_transform_list = [
    basic_transforms.apply_hash,
]
_transform_map = {
    transform.name: transform for transform in _transform_list
}
