
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


number = 12345
result = sum_of_digits(number)
print("Sum of digits:", result)

