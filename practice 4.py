#Dictionarys
dict = {
    "name": "Talha",
    "age": 20,
    "city": "Lahore",
    "weight": 70.67,
    "language": ["Python", "JavaScript"],
    "IsAdult": True
}
print(dict)
print(dict["name"])
print(dict["language"])
dict["age"] = 21
print(dict)

null_dict = {}
null_dict["name"] = "Talha"
print(null_dict)

dict1 = {
    "name": "Talha",
    "age": 20,
    "dict2": {
        "University": "CUI",
        "Department": "CS",
        "CGPA": 3.5,
        "Semester": 4
    }
}
print(dict1)
print(dict1["dict2"]["CGPA"])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
print(dict.update({"name": "Ali"}))
