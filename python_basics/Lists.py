a = [1, 2, 3, 4, 5.6, "Srini", [22, 33], [1, [2, 4]]]
print(a.index(2))
print(a.count(1))
# print("Reverse:", a.reverse())
print(a)
print(a.pop(1))
print(a)
a.append(99)
print(a)

a += [77, 88, 99]
print(a)

print(a[3])
print(a[6][1])