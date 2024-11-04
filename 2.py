def get_digit(number):
    return number % 10 + (number // 10 % 10)

def sum_odd(number):
    result=0
    
    for i in range(len(number) - 1, -1, -2):
        result += int(number[i])
    return result

def sum_even(number):
    result=0
    for i in range(len(number) - 2, -1, -2):
        result += get_digit(int(number[i]) * 2)
    return result

while True:
    number = input("Enter a valid credit card number: ")
    if not number.isdigit():
        print("Invalid input. Please enter numeric values only.")
        continue
    
    result=sum_even(number)+sum_odd(number)
    
    if result%10==0:
        print("Valid Credit Card")
    else:
        print("Invalid Credit Card")
    break  

