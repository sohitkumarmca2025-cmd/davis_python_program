# Check number within range

num = int(input("Enter number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low <= num <= high:
    print("Number is within range")
else:
    print("Number is outside range")

# Output:
# Enter number: 15
# Enter lower limit: 10
# Enter upper limit: 20
# Number is within range
