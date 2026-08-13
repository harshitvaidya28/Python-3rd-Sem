
lst = [100, 50, 400, 500]

lst[1] = 200
print("After changing second element to 200:")
print(lst)


lst.append(600)
print("\nAfter appending 600:")
print(lst)


lst.insert(2, 300)
print("\nAfter inserting 300 at index 2:")
print(lst)

lst.remove(600)
print("\nAfter removing 600:")
print(lst)

lst.pop(0)
print("\nAfter removing element at index 0:")
print(lst)

