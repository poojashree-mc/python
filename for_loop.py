for each_num in range(1, 10):
    print("<- This is for loop test -->", each_num, each_num  * "Pooja  ")
    if each_num == 67:
        break
else:
    print("AAA and failed......")

for x in range(5):
    for y in range(3):
        print(f"VALL = ({x}, {y})")

nunm = 1
while nunm < 100:
    nunm += 1
    print("Vall ",  nunm)


cmd = ""
while cmd != "quit":
    cmd = input("Enter the value :: ")



def greet_check(num, by):
    print("Welcome !!!!", num+by)

greet_check(3, by = 1)

def greet_check(num, by = 1):
    print("Welcome !!!!", num+by)

greet_check(3, by = 5)