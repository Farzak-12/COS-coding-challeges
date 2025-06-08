decimal = int(input("Input you decimal number: "))
binary_list = [] #list to store binary digits
while decimal: 
    bin = decimal%2 # get the remainder
    decimal = decimal // 2 
    binary_list.insert(0,bin) #insert at the beginning of the list
print("The binary equvalent of your number is ",*binary_list, sep="") #print the list as a string without spaces

binary = input('Input your binary number: ')
pow = len(binary) - 1 #calculate the power of 2
final_dec = 0 #variable to store the final decimal value
for number in binary:
    final_dec += int(number)*(2**pow) #calculate the decimal value
    pow -= 1 #decrease the power of 2
print("The binary equvalent of your number is ", final_dec)