#These are different types of loops

print("\n-----while----")
#while - loop that executes WHILE some condition remains true
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}")



print("\n----for-----")
#for - executes a block of code a fixed number of times.
for x in range(1, 11): #keeps going until x becomes 11 (it stops printing at 10)
    print(x)

#you can do various things like reversed(range(1,11))
#or you could do steps. range(1,11,2 <- step) this will add up depending on your step


print("\n----continue-----")
#you can skip a number using "continue"
for x in range(1,11):
    if x == 5:
        continue
    else:
        print(x)


print("\n-----break-----")
#meanwhile you can get out of a loop using "break"
while True:
    number = int(input("Enter number: "))
    if number <= 0:
        print("Number must be greater than 0")
    else:
        break


print("\n-----nested-loop-----")
#a loop within a loop
for x in range(3):
    for i in range(1,10):
        print(i, end="-")
    print()
