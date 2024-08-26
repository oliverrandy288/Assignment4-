# 1. Python List Transformation
print("Task 1: Python List Transformation")

# Given list of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order
grades.sort(reverse=True)
print("Sorted grades in descending order:", grades)

# Calculate the average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

print("\n")  # New line for separation

# 2. Advanced List Methods and Identity Operators
print("Task 2: Advanced List Methods and Identity Operators")

# Given lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if Alice is in both lists
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted their assignment and attended class.")
else:
    print("Alice did not meet both criteria.")

print("\n")  # New line for separation

# 3. Advanced Slicing Techniques
print("Task 3: Advanced Slicing Techniques")

# Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract temperatures for the second week (index 7 to index 14)
second_week_temps = temperatures[7:14]
print("Temperatures for the second week:", second_week_temps)

# Extract all temperatures above 100
above_100_temps = [temp for temp in temperatures if temp > 100]
print("Temperatures above 100:", above_100_temps)
