
n = int(input("enter a number :"))

result = []
n1 = 0
n2 = 1
c = 0
for i in range(n):
    print(n1)
    c = n1 + n2
    n1 = n2
    n2 = c
