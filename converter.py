decimal = int(input("Input you decimal number: "))
binary_list = [] #
while decimal:
    bin = decimal%2
    decimal = decimal // 2
    binary_list.insert(0,bin)
print("The binary equvalent of your number is ",*binary_list, sep="")

binary = input('Input your binary number: ')
pow = len(binary) - 1
final_dec = 0
for number in binary:
    final_dec += int(number)*(2**pow)
    pow -= 1
print("The binary equvalent of your number is ", final_dec)