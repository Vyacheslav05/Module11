import inspect
from pprint import pprint
def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = {attr: getattr(obj, attr) for attr in dir(obj) if
                          not callable(getattr(obj, attr)) and not attr.startswith('__')}
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    info['module'] = inspect.getmodule(obj)

    if isinstance(obj, int):
        info['bit_length'] = obj.bit_length()
    elif isinstance(obj, str):
        info['length'] = len(obj)
    elif isinstance(obj, list):
        info['length'] = len(obj)
        info['first_element'] = obj[0] if len(obj) > 0 \
            else None

    return info

number_info = introspection_info(42)
pprint(number_info)