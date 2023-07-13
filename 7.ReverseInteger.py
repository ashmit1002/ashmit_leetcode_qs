x = -123

result = ""
is_negative = False
if x < 0:
    x *= -1
    is_negative = True

x = str(x)
i = 1

for digit in list(reversed(x)):
    result += digit
result = int(result)
if is_negative == True:
    result *= -1

if result <= -2**31 or result >= 2**31 - 1:
    print(0)
    quit()

print(result)