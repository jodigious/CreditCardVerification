'''
Work out Luhn's algorithm.
'''

# Sample credit card number for use with this program
# https://saijogeorge.com/dummy-credit-card-generator/

#credit_card = 4757789945729320
#credit_card = 4370366259700473
#credit_card = 4111111111111111
credit_card = 37562198673


######
print("Here is our credit card number")
credit_card_array = [int(num) for num in str(credit_card)]
print(credit_card_array)

print("\nAnd our checksum is")
checksum = credit_card_array.pop(-1)
print(checksum)

luhn = []
new_luhn = []
final_luhn = 0

def revArray(lst):
    return lst[::-1]

######
print("\nNow, starting from the rightmost digit, we double every second number")

rev_cc = revArray(credit_card_array)

for i in range(len(rev_cc)):
    if i%2 == 0: 
        luhn.append(rev_cc[i]*2)
    else:
        luhn.append(rev_cc[i])

print(revArray(luhn))

######
print("\nIf the doubled digit is more than 9, we add the digits")

for num in luhn:
    if num > 9:
        digits = [int(i) for i in str(num)]
        sums = digits[0] + digits[1]
        new_luhn.append(sums)
    else:
        new_luhn.append(num)

print(revArray(new_luhn))

#####
print("\nNow we add all the digits, and multiply by 9")        
final_luhn = sum(new_luhn) * 9
print(final_luhn)

print("\nwith a verification unit of")
verification = [int(num) for num in str(final_luhn)]
print(verification)

print("\nNow we check the verification unit against the checksum\n")
if verification[-1] is not checksum:
    print("This is NOT a valid credit card.")
else:
    print("This is a valid credit card.")

luhn

