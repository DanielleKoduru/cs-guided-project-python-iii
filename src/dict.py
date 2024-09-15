"""
Add "Herb" to the phonebook with the number 7653420789.
Remove "Bill" from the phonebook.
"""
phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}
​
print(phonebook["Bill"])
​
phonebook["Herb"] = 7653420789 
​
phonebook["Abe"] = 11111111111
​
del phonebook["Barry"]
​
if "Herb" in phonebook:
    print("Yes") 
else:
    print("No")
​
print(phonebook.values())
print(phonebook.items())
​
for (key, value) in phonebook.items():
    print(key, value)
    # print(value)