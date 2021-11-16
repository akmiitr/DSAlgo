# Write a function to flatten a nested dictionary. Namespace the keys with a period.
#
# For example, given the following dictionary:
#
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
#
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }


def _flatten(d, sep=".", parent_key=""):
    items = []
    for key, value in d.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            items.extend(_flatten(value, sep=".", parent_key=new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)


if __name__ == "__main__":
    print(_flatten({
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }))