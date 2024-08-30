import inspect
from random import randint


class Example:
    def __init__(self, attr):
        self.attribute = attr

    def some_func(self):
        print("doing something")


def introspection_info(obj):
    info = {}
    info["type"] = type(obj).__name__
    if hasattr(obj, "attribute"):
        info["attributes"] = getattr(obj, "attribute")
    else:
        info["attributes"] = "..."
    info["methods"] = dir(obj)
    if inspect.getmodule(obj):
        info["module"] = inspect.getmodule(obj).__name__
    else:
        info["module"] = inspect.getmodule(obj)
    return info


ob = Example(5)
number_info = introspection_info(ob)
print(number_info)

number_info = introspection_info(42)
print(number_info)

number_info = introspection_info(randint)
print(number_info)
