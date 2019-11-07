# tuples assignment

# question 1
tup1 = tuple(i**2 for i in range(1, 51))
tup2 = tuple([chr(65+i)*(i+1) for i in range(26)])

print(tup1)
print(tup2)


# program that takes two tuples tup1 and tup2, returns true if every element of tup1 is also an element of tup2

t1 = tuple(eval(input("enter tup1")))
t2 = tuple(eval(input("enter tup2")))

if set(t1).issubset(set(t2)):
    print( True)
else:
    print(False)

