print "CMPT 120 Assignment #1"
print "Created by Wen Xuan Xie (wxxie@sfu.ca)"
print "Date of last revision: September 19, 2014 "
print "Approximate number of hours used: approximately 1 hour"
print "---------------------------------------------------------"
print "Hello, this is the CMPT 120 Electronic components factory system!"
print "This factory's device requires 11 A components and 4 B components "
print "You will be able to calculate number of components needed"
print "to produce a number of devices,"
print "and also the number of devices that can be produced given the components and"
print "how many components remain "
print "Please follow the system prompts "
print "---------------------------------------------------------"

print "process (a)"
print " "
numeric_var = input ("How many devices you need to produce? " )

compo_A = numeric_var * 11
compo_B = numeric_var * 4

print "To produce " + str(numeric_var) + " device(s), you need to have " + str(compo_A)+ " A's components and " + str(compo_B) + " B's components."
print " "

print "process (b)"
print " "
varA = input("How many A's do you have? ")
varB = input("How many B's do you have? ")

total_device_A = varA / 11
total_device_B = varB / 4

remainder_A = varA - total_device_A*11
remainder_B = varB - total_device_B*4

if (total_device_A < total_device_B):
    print "With the number of components you have now, you can produce " + str(total_device_A) + " devices,"
    remainder_A = varA - total_device_A*11
    remainder_B = varB - total_device_A*4
    print "and there will be " + str(remainder_A) + " A's remaining and " + str(remainder_B) + " B's remaining." 
else:
    print "With the number of components you have now, you can produce " + str(total_device_B) + " devices,"
    remainder_A = varA - total_device_B*11
    remainder_B = varB - total_device_B*4
    print "and there will be " + str(remainder_A) + " A's remaining and " + str(remainder_B) + " B's remaining."
  
print " "
print "This is the end of the program! Bye bye!"




