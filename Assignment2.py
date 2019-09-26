def welcome_message():
    print "CMPT 120 Assignment #2"
    print "Author: Wen Xuan Xie (wxxie@sfu.ca)"
    print "Date of last revisiom: September 23, 2014"
    print "Approximate hours used: Approximately 6 hours"
    print " "
    return

welcome_message()

import math
import re

name= raw_input("Please provide your  first and last names,\n seperated by a space: ")
address = raw_input ("Please provide your address, number first,\n and then the street: ")
binaryA = input ("Please provide a binary number of 2 to 4 bits: ")
characterA = raw_input("Please provide a two character code with any combination \n of letters, symbols, or number: ")

print " "
print "Calculating n1..."

address_number = int(re.match( '\d+', address).group())

string_address_number=str(address_number)
address_second_last=string_address_number[-2:]
int_second_last=int(address_second_last)

pi = math.pi
sqrt_second_last = math.sqrt(int_second_last)
sum_one= pi + sqrt_second_last

print "TRACE last two digits in address: " + str(address_second_last)
print "TRACE square root of the last two digits: " + str(sqrt_second_last)
print "TRACE sum of pi + sqrt of last two digits in address: " + str(sum_one)

if (binaryA %2 == 0):
    round_sum = round(sum_one,2)
    print "TRACE the binary number is even, rounded to two digits in address: "+str(round_sum)
    str_sum=str(round_sum)
    starter = str_sum[-2:]
    str_sum_lastone = str_sum[-1]
    str_sum_lasttwo = str_sum[-2]
    apple = int(str_sum_lastone) + int(str_sum_lasttwo) 
else:
    round_sum = round(sum_one,1)
    print "TRACE the binary number is odd, rounded to one digits in address: " + str(round_sum)
    str_sum=str(round_sum)
    starter = str_sum[-1:]
    
     

if (len(starter)== 1): 
    print "TRACE digits in the fractional part after rounding: " + str(starter)
    n1 = str(starter)
    print "TRACE n1 is " + str(n1)
else:
    print "TRACE digits in the fractional part after rounding: " + str(starter)
    n1 = str(apple)
    print "TRACE n1 is " + str(n1)
   


print " "
print "Constructing the password..."

str_name = name
first_name, last_name = str_name.split()

last_index_one = last_name[1]
first_index_zero = first_name[0]
last_upper = last_index_one.upper()
first_lower = first_index_zero.lower()


last_A=last_name[-1]
last_B=last_A.upper()
last_countA=address.count(last_A)
last_countB=address.count(last_B)
sum_last=last_countA+last_countB

question_mark = "?"*int(n1)


int_set = set('0123456789!@#$%^&*_-+={[}]|\:;<,>.?/')
if any((x in int_set) for x in characterA):
    binary_final =characterA[1]
    
else:
    binary_final= characterA
    

password_beta = last_upper + n1 + str(question_mark)+ first_lower + str(sum_last) + str(binary_final)

length_password = len(password_beta)

if (length_password%2==0):
    last_code="E"
else:
    last_code="O"
    
    
print "TRACE n2 - times the last letter in last name is in address \n both in lower and upper case: " + str(sum_last)
print "TRACE whole or part code to attach: " + str(binary_final)
print "TRACE password up until before checking length: " + str(password_beta)
print "TRACE length of password so far: " + str(length_password)


password = last_upper + n1 + str(question_mark)+ first_lower + str(sum_last) + str(binary_final) + str(last_code)
print" "
print "Here is your password!! " + password
print" "
print "Thank you for using my password service! Have a good one!"
