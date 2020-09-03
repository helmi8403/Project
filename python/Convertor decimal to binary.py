number = (input("Enter Base 10 number [1-255]: "))

number = float(number)

num1 = number - 128


if num1 < 0:
    num1 = 0
    numA = number
else:
    num1 = 1
    numA = number - 128

num2 = numA - 64

if num2 < 0:
    num2 = 0
    numB = numA
else:
    num2 = 1
    numB = numA - 64

num3 = numB - 32

if num3 < 0:
    num3 = 0
    numC = numB
else:
    num3 = 1
    numC = numB - 32

num4 = numC - 16


if num4 < 0:
    num4 = 0
    numD = numC
else:
    num4 = 1
    numD = numC - 16

num5 = numD - 8


if num5 < 0:
    num5 = 0
    numE = numD
else:
    num5 = 1
    numE = numD - 8

num6 = numE - 4

if num6 < 0:
    num6 = 0
    numF = numE
else:
    num6 = 1
    numF = numE - 4

num7 = numF - 2

if num7 < 0:
    num7 = 0
    numG = numF
else:
    num7 = 1
    numG = numF - 2

num8 = numG - 1


if num8 < 0:
    num8 = 0
    numH = numG
else:
    num8 = 1
    numH = numG - 1


print(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8))