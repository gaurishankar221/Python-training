"""a="hello world"
b="hello python"
print(a)
print(b)

a="hello python"
print(len(a))

b="good character"
print(len(a))

x="The best thing about python is its syntax"
print("best"in x)

b="the best thing about football is about rules"
if "football"in a:
    print("yes")

text="python"
print(text[:5])

x="heloo"
print(x[1:])
print(x[-5:-1])

y="     hello"
print(y.upper())
print(y.strip())


z="apple,mango,banana"
print(z.strip(','))


for i in range(1, 11):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()


    

 name = input("Enter your name: ")

count = 0

for i in name:
    if i.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)"""

for i in range(5):
    print(i)
    if i==3:
        break
    name="python"
    print(f"hi my name is {name} and i am famous for ml,dl")
