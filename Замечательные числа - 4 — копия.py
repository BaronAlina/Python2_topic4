a = int(input())
b = int(input())
a1 = a // 1000
b1 = a // 100 % 10
while (((a1 * 10 + b1) * 10 + b1) * 10 + a1) <= b:
    b1 = b1 + 1
    if ( b1 > 9):
        a1 = a1 + 1
        b1 = 0
        print(a1, b1, b1, a1, sep="")
