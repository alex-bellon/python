import ast

dict_str = "{'foo': 'bar', 'dead': 'beef'}"

print(type(dict_str))

dict_str = ast.literal_eval(dict_str)

print(type(dict_str))
