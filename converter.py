decimal = int(input("Input your decimal number: "))
binary_list = [] #list to store binary digits
while decimal: 
    temp_bin = decimal%2 # get the remainder
    decimal = decimal // 2 
    binary_list.insert(0,temp_bin) #insert at the beginning of the list
print("The binary equivalent of your number is ",*binary_list, sep="") #print the list as a string without spaces

binary = input('Input your binary number: ')
power = len(binary) - 1 #calculate the power of 2
final_dec = 0 #variable to store the final decimal value
for number in binary:
    final_dec += int(number)*(2**power) #calculate the decimal value
    pow -= 1 #decrease the power of 2
print("The decimal equivalent of your number is ", final_dec)