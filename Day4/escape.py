"""b="it's me python"
print(b)

a="hello\n world"
print(a)
mylist=["mango","apple","orange"]
print(mylist)

print(type(mylist))

print(mylist[0])
print(mylist[1])
mylist1=["1","true","0.25"]
print(mylist1)
print(len(mylist1))

my_list2=["apple",1,"mano"]
print(my_list2[-1])
country=["portugal","france","england","norway","france"]
if "portugal"in country:
    print("yes")

    mylist4=["apple","mango","banana"]
    print(mylist4)
    mylist4[1]="litchi"
    print(mylist4)
    mylist4[0:2]=["portugal","argentina"]
    print(mylist4)
    mylist4[0:1]=["python","django"]
    print(mylist4)
    print(len(mylist4))


    myitem=["apple","mango","banana"]
    myitem.insert(0,"orange")
    print(myitem)

    list1=["ram","sita"]
    list2=["hari","krishna"]
    list1.extend(list2)
    print(list1)


    mylist7=["apple","banana","mango"]
    del mylist7[0]
    print(mylist7)
    country=["nepal","pakistan","india"]
    country.sort()
    print(country)
    country.sort(reverse=True)
    print(country)
    a=["apple","mango","banana"]
    b=["football","cricket","basketball"]
    for i in b:
        print(a)

        a.append(i)
    
    mylist7=["apple","banana","orange"]
    print(mylist7)
    b=mylist7.copy()
    b.append("football")
    print(b)
    print(mylist7)"""


"""nums = [1, 2, 3, 4, 5]

squares = []

for i in nums:
    squares.append(i * i)

print(squares)"""

"""num = [1, 2, 3, 4, 5]
sum = 0

for i in num:
    sum = sum + i

print(sum)"""

num = [1, 2, 3, 4, 5]

max_value = num[0]

for i in num:
    if i > max_value:
        max_value = i

print(max_value)