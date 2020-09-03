number = (input("enter Base 2 number: "))



num1 = number[0]
num2 = number[1]
num3 = number[2]
num4 = number[3]
num5 = number[4]
num6 = number[5]
num7 = number[6]
num8 = number[7]



if float(num1) < 1:
    num1 = 0
else:
    num1 = 128


if float(num2) < 1:
    num2 = 0
else:
    num2 = 64

if float(num3) < 1:
    num3 = 0
else:
    num3 = 32

if float(num4) < 1:
    num4 = 0
else:
    num4 = 16

if float(num5) < 1:
    num5 = 0
else:
    num5 = 8


if float(num6) < 1:
    num6 = 0
else:
    num6 = 4


if float(num7) < 1:
    num7 = 0
else:
    num7 = 2

if float(num8) < 1:
    num8 = 0
else:
    num8 = 1

numX = float(num1) + float(num2) + float(num3) + float(num4) + float(num5) + float(num6) + float(num7) + float(num8)

print(numX)

