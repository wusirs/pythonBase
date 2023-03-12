# json 转换
import json

data = [
    {
        'name': '张大山',
        'age': 11
    },
    {
        'name': '王大锤',
        'age': 12
    },
    {
        'name': '李四',
        'age': 15
    }
]

# ensure_ascii=False 这么设置就不会吧中文转成ascii码值了
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

obj = json.loads(json_str)
print(type(obj))
print(obj)


print(json.loads('[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 12}, {"name": "李四", "age": 15}]'))