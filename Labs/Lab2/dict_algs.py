ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }]
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }]
}

emps = [ivan, darja]


def emps_adult_children(emps_):
    emps_with_adult_children = []
    for emp in emps_:
        for x in emp["children"]:
            if x["age"] > 18:
                emps_with_adult_children.append(emp["name"])
                break
    for y in emps_with_adult_children:
        print(y)


print('Работники с совершеннолетними детьми:')
emps_adult_children(emps)
