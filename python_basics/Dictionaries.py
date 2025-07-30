a = {"name": "Srini", "age": 32, "height": 5.2, "list": [11, 22, "Hello"], "my_internal_dict": {"first": 1}}
print(a)
print(a.items())
print(a.values())
print(a.pop("name"))
print(a)
print(a.get("age"))
print(a)

a.update({"address": "bangalore"})
print(a)
print(a.popitem())
print(a)
