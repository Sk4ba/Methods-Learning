#indexing - accessing elements of a sequence using [] (indexing operator)
#basically an array thingy
#[start: end: step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0]) #prints the chosen digit
print(credit_number[-1]) #prints the last digit the higher the negative is
print(credit_number[0:4]) #starts from the chosen digit to ending digit
print(credit_number[5:]) #starts from the chosen digit upto the end
print(credit_number[::2]) #steps prints every chosen character in the string
print(credit_number[::-1]) #reverses the whole string