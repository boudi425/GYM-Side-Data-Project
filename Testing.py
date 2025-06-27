listOfNames = {
            "abdo": {"Hobby": ["Coding"]},
            "ali": {"Hobby": "Reading"},
            "Speed": {"Hobby": "Running"}
            }
List = ["Coding", "Reading"]
NewList = ", ".join(List)
for key, value in listOfNames.items():
    print(value)
    print(value["Hobby"])
    for i in listOfNames[key]:
        print(i)
print(NewList)