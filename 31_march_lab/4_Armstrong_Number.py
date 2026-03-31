num = 153

digits = len(str(num))
temp = num
result = 0

while temp:
    digit = temp % 10
    result += digit ** digits
    temp //= 10

print("Is Armstrong Number:", result == num)
