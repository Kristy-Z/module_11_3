import inspect


def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', None),
    }

    if hasattr(obj, '__class__'):
        info['class'] = obj.__class__.__name__

    if inspect.isfunction(obj) or inspect.ismethod(obj):
        info.update({
            'signature': str(inspect.signature(obj)),
            'source_code': inspect.getsource(obj),
            'file': inspect.getfile(obj),
            'line_number': inspect.getsourcelines(obj)[1]
        })

    return info


number_info = introspection_info(42)
print(number_info)
