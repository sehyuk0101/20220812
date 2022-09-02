hi = "hello there"

name = "ana"
greet = hi + name
greeting = hi + " " + name

silly = hi + " " + name * 3

x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x=", x)
print("my fav num is " +x_str + ". " + "x =" + x_str)

text = input("Type anything...")
print(5*text)

num = int(input("Type a number..."))
print(5*num)

mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5,11,2):
    mysum += i
    if mysum == 5:
        break
print(mysum)

n = 0
while n<5:
    print(n)
    n = n + 1

for n in range(5):
    print(n)