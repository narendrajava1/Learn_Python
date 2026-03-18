# List (Ordered & Mutable)
numbers = [1, 2, 3, 4]
names = ["Ram", "Shyam", "Hari"]
numbers[0] = 10
print(numbers)
# Tuple (Ordered & Immutable)
points = (1, 2, 3)
print(points)
# Set (Unordered & Unique)
unique_numbers = {1, 2, 3, 3}
print(unique_numbers)   # {1, 2, 3}
# Dictionary (Key-Value Pair)
student = {
    "name": "Narendra",
    "age": 25
}
print(student["name"])   # Narendra
# Check Data Type
print(type(student["age"]))
# Dynamic Typing (Important ⭐)
x = 10
x = "Hello"
print(x)
print(type(x))