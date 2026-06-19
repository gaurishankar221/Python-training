"""count=0
while count<5:
    count+=1
    print(count)

    while TRUE:
        print("infinite loops")"""

"""count = 1

while count <= 5:
    print(count)

    if count == 3:
        break

    count += 1"""

"""count = 0

while count <= 5:
    count += 1

    if count == 3:
        continue

    print(count)"""

"""sum=0
count=0

while count <5:
    count+=1
    sum+=count
    print(sum)"""

text = ""

while text != "exit":
    text = input("Enter something (type 'exit' to stop): ")

    if text == "exit":
        print("Program stopped.")
        break

    print("You entered:", text)
