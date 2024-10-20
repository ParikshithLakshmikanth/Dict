mydict = {}

mydict={1:"Apple",2:"Ball"}

mydict={"name":"John",1:[2,4,3]}
mydict={"name":"Jack","age":23}
print(mydict["name"])
print(mydict.get("age"))

mydict["age"] = 27
print(mydict)

mydict["address"] = "Downtown"
print(mydict)

print("Address:",mydict["address"])

mydict.clear()

print(mydict)