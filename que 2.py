# Initial list
lst = [100, 50, 400, 500]

# Change Element: Change the second element to 200
lst[1] = 200
print("After changing second element to 200:")
print(lst)

# Append Element: Add 600 to the end
lst.append(600)
print("\nAfter appending 600:")
print(lst)

# Insert Element: Insert 300 at index 2
lst.insert(2, 300)
print("\nAfter inserting 300 at index 2:")
print(lst)

# Remove Element (by value): Remove 600
lst.remove(600)
print("\nAfter removing 600:")
print(lst)

# Remove Element (by index): Remove element at index 0
lst.pop(0)
print("\nAfter removing element at index 0:")
print(lst)

