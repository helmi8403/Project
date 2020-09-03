number = input("Enter Subnet Slash Notation: ")

number = int(number)

if number == 8:
    subnet = "255.0.0.0"
    totalHost = "16,777,216"
    noOfsubnet = "0"


elif number == 9:
    subnet = "255.128.0.0"
    totalHost = "8,388,606"
    noOfsubnet = "2 (0)"


elif number == 10:
    subnet = "255.192.0.0"
    totalHost = "4,194,302"
    noOfsubnet = "4 (2)"


elif number == 11:
    subnet = "255.224.0.0"
    totalHost = "2,097,150"
    noOfsubnet = "8 (6)"


elif number == 12:
    subnet = "255.240.0.0"
    totalHost = "1,048,574"
    noOfsubnet = "16 (14)"


elif number == 13:
    subnet = "255.248.0.0"
    totalHost = "524,286"
    noOfsubnet = "32 (30)"


elif number == 14:
    subnet = "255.252.0.0"
    totalHost = "262,142"
    noOfsubnet = "64 (62)"


elif number == 15:
    subnet = "255.254.0.0"
    totalHost = "131,070"
    noOfsubnet = "128 (126)"


elif number == 16:
    subnet = "255.255.0.0"
    totalHost = "65,534"
    noOfsubnet = "256 (254)"


elif number == 17:
    subnet = "255.255.128.0"
    totalHost = "32,766"
    noOfsubnet = "512 (510)"


elif number == 18:
    subnet = "255.255.192.0"
    totalHost = "16,382"
    noOfsubnet = "1,024 (1,022)"


elif number == 19:
    subnet = "255.255.224.0"
    totalHost = "8,190"
    noOfsubnet = "2,048 (2,046)"


elif number == 20:
    subnet = "255.255.240.0"
    totalHost = "4,094"
    noOfsubnet = "4,096 (4,094)"


elif number == 21:
    subnet = "255.255.248.0"
    totalHost = "2,046"
    noOfsubnet = "8,192 (8,190)"


elif number == 22:
    subnet = "255.255.252.0"
    totalHost = "1,022"
    noOfsubnet = "16,384 (16,382)"


elif number == 23:
    subnet = "255.255.254.0"
    totalHost = "510"
    noOfsubnet = "32,768 (32,766)"


elif number == 24:
    subnet = "255.255.255.0"
    totalHost = "254"
    noOfsubnet = "65,536 (65,534)"


elif number == 25:
    subnet = "255.255.255.128"
    totalHost = "126"
    noOfsubnet = "131,072 (131,070)"


elif number == 26:
    subnet = "255.255.255.192"
    totalHost = "62"
    noOfsubnet = "262,144 (262,142)"


elif number == 27:
    subnet = "255.255.255.224"
    totalHost = "30"
    noOfsubnet = "524,288 (524,286)"


elif number == 28:
    subnet = "255.255.255.240"
    totalHost = "14"
    noOfsubnet = "1,048,576 (1,048,574)"


elif number == 29:
    subnet = "255.255.255.248"
    totalHost = "6"
    noOfsubnet = "2,097,152 (2,097,150)"


elif number == 30:
    subnet = "255.255.255.252"
    totalHost = "2"
    noOfsubnet = "4,194,304 (4,194,302)"




print("Your subnet: " + subnet)
print("Your total number of host: " + totalHost)
print("Your total number of subnets: " + noOfsubnet)