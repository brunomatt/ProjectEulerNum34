# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
answer = 0

def factorial(int):
    value = 1
    for k in range(1, int + 1):
        value = k * value
    return value

for i in range(3,99999):
    num = 0
    for digit in str(i):
        num = num + factorial(int(digit))
    if num == i:
        answer += num

print(answer)

