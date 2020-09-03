number = (input("Enter Base 1st Octet [1-255]: "))
number1 = (input("Enter Base 2nd Octet [1-255]: "))
number2 = (input("Enter Base 3rd Octet [1-255]: "))
number3 = (input("Enter Base 4th Octet [1-255]: "))

oct1 = number
oct2 = number1
oct3 = number2
oct4 = number3

print()
print("Your IP address in Decimal: " + oct1 + "." + oct2 + "." + oct3 + "." + oct4)


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



number1 = float(number1)

num11 = number1 - 128


if num11 < 0:
    num11 = 0
    numA1 = number1
else:
    num11 = 1
    numA1 = number1 - 128

num21 = numA1 - 64

if num21 < 0:
    num21 = 0
    numB1 = numA1
else:
    num21 = 1
    numB1 = numA1 - 64

num31 = numB1 - 32

if num31 < 0:
    num31 = 0
    numC1 = numB1
else:
    num31 = 1
    numC1 = numB1 - 32

num41 = numC1 - 16


if num41 < 0:
    num41 = 0
    numD1 = numC1
else:
    num41 = 1
    numD1 = numC1 - 16

num51 = numD1 - 8


if num51 < 0:
    num51 = 0
    numE1 = numD1
else:
    num51 = 1
    numE1 = numD1 - 8

num61 = numE1 - 4

if num61 < 0:
    num61 = 0
    numF1 = numE1
else:
    num61 = 1
    numF1 = numE1 - 4

num71 = numF1 - 2

if num71 < 0:
    num71 = 0
    numG1 = numF1
else:
    num71 = 1
    numG1 = numF1 - 2

num81 = numG1 - 1

if num81 < 0:
    num81 = 0
    numH1 = numG1
else:
    num81 = 1
    numH1 = numG1 - 1




number2 = float(number2)

num12 = number2 - 128


if num12 < 0:
    num12 = 0
    numA2 = number2
else:
    num12 = 1
    numA2 = number2 - 128

num22 = numA2 - 64

if num22 < 0:
    num22 = 0
    numB2 = numA2
else:
    num22 = 1
    numB2 = numA2 - 64

num32 = numB2 - 32

if num32 < 0:
    num32 = 0
    numC2 = numB2
else:
    num32 = 1
    numC2 = numB2 - 32

num42 = numC2 - 16


if num42 < 0:
    num42 = 0
    numD2 = numC2
else:
    num42 = 1
    numD2 = numC2 - 16

num52 = numD2 - 8


if num52 < 0:
    num52 = 0
    numE2 = numD2
else:
    num52 = 1
    numE2 = numD2 - 8

num62 = numE2 - 4

if num62 < 0:
    num62 = 0
    numF2 = numE2
else:
    num62 = 1
    numF2 = numE2 - 4

num72 = numF2 - 2

if num72 < 0:
    num72 = 0
    numG2 = numF2
else:
    num72 = 1
    numG2 = numF2 - 2

num82 = numG2 - 1


if num82 < 0:
    num82 = 0
    numH2 = numG2
else:
    num82 = 1
    numH2 = numG2 - 1


number3 = float(number3)

num13 = number3 - 128


if num13 < 0:
    num13 = 0
    numA3 = number3
else:
    num13 = 1
    numA3 = number3 - 128

num23 = numA3 - 64

if num23 < 0:
    num23 = 0
    numB3 = numA3
else:
    num23 = 1
    numB3 = numA3 - 64

num33 = numB3 - 32

if num33 < 0:
    num33 = 0
    numC3 = numB3
else:
    num33 = 1
    numC3 = numB3 - 32

num43 = numC3 - 16


if num43 < 0:
    num43 = 0
    numD3 = numC3
else:
    num43 = 1
    numD3 = numC3 - 16

num53 = numD3 - 8


if num53 < 0:
    num53 = 0
    numE3 = numD3
else:
    num53 = 1
    numE3 = numD3 - 8

num63 = numE3 - 4

if num63 < 0:
    num63 = 0
    numF3 = numE3
else:
    num63 = 1
    numF3 = numE3 - 4

num73 = numF3 - 2

if num73 < 0:
    num73 = 0
    numG3 = numF3
else:
    num73 = 1
    numG3 = numF3 - 2

num83 = numG3 - 1


if num83 < 0:
    num83 = 0
    numH3 = numG3
else:
    num83 = 1
    numH3 = numG3 - 1



oct_1 = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8)
oct_2 = str(num11) + str(num21) + str(num31) + str(num41) + str(num51) + str(num61) + str(num71) + str(num81)
oct_3 = str(num12) + str(num22) + str(num32) + str(num42) + str(num52) + str(num62) + str(num72) + str(num82)
oct_4 = str(num13) + str(num23) + str(num33) + str(num43) + str(num53) + str(num63) + str(num73) + str(num83)



print( "Your IP address in binary: " + oct_1 + "." + oct_2 + "." + oct_3 + "." + oct_4)