x = 5,6,5,6

y = [5,6,5,6,5,46,5,8,2,14,6,6]

print(x[1])
print(y[2])

#adds an element to end of list
y.append(2)
print(y)

#insert at (position,data)
y.insert(2,99)
print(y)

#remove a nos first apperence with y.remove(no) and for index position
y.remove(y[2])
print(y)

#Slicing
print(x[2:7])

#acess from behind
print(x[-1])

#getting index value of a no
print(y.index(6))

#count of a value
print(y.count(6))

#sorting
y.sort()
print(y)

#Multi-Dimensational List
x = [
    [5,6],
    [6,7],
    [7,8],
    [2,5]
    ]

print(x[1][0])
