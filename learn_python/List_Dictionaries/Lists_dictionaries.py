# A list is a collection of items stored in order.
numbers = [10, 20, 30, 40]
names = ["Ram", "Shyam", "Narendra"]
mixed = [1, "hello", 3.5]
# Access Elements
print(names[0])   # Ram
print(names[-1])  # Narendra (last element)
# Modify List
numbers = [10, 20, 30]
numbers[1] = 50

print(numbers)   # [10, 50, 30]
# Common List Operations
# ➤ Add elements
numbers = [1, 2]

numbers.append(3)       # [1, 2, 3]
numbers.insert(1, 10)   # [1, 10, 2, 3]
print(numbers)
# Remove elements
numbers = [1, 2, 3, 4]

numbers.remove(2)   # removes value
numbers.pop()       # removes last
print(numbers)
# ➤ Other useful methods
nums = [3, 1, 4]

nums.sort()    # [1, 3, 4]
nums.reverse()  # [4, 3, 1]
print(len(nums))       # length
print(nums)
# 🔸 Loop through List
for num in nums:
    print(num)
# 🔸 List Comprehension(🔥 Important)
squares=[x*x for x in nums]
print(squares)
# 🔹 2. Python Dictionaries
#
# A dictionary stores data in key-value pairs.
student = {
    "name": "Narendra",
    "age": 25,
    "marks": 90
}
print(student)
# 🔸 Access Values
print(student["name"])     # Narendra
print(student.get("age"))  # 25
# 🔸 Modify Dictionary
student["age"] = 26
student["city"] = "Hyderabad"
print(student)
# 🔸 Remove Items
student.pop("marks")
del student["age"]
print(student)
# 🔸 Loop through Dictionary
print(student.keys())
print(student.values())
print(student.items())
for(key,value) in student.items():
    print("this is the key:"+key)
    print(value)

#🔹 4. Real-Time Example (🔥 Useful for You)
# Trading Example
portfolio = [
    {"stock": "NIFTY", "price": 150, "qty": 10},
    {"stock": "BANKNIFTY", "price": 200, "qty": 5}
]
for option_index in portfolio:
    profit=option_index["price"]*option_index["qty"]
    print(option_index["stock"],profit)
# 🔹 Summary
#
# ✔ List → ordered collection
# ✔ Dictionary → key-value mapping
# ✔ Lists use index, dictionaries use keys