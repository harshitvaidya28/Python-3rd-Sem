
numbers = [10, 20, 30, 40, 50]

# Access the third element (index 2)
try:
	third_element = numbers[2]
	print("Third element:", third_element)
except IndexError:
	print("Third element: List has fewer than 3 elements")

# List length
print("List length:", len(numbers))

# Check if the list is empty
if numbers:
	print("List is not empty")
else:
	print("List is empty")
