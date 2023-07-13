s = "     -4193 with words"
result = ""
for i in s:
    try:
        digit = int(i)
    except:
        continue
    result += str(digit)
    try:
        if s.index(result) - 1 == s.index("-"):
            result = -1 * int(result)
    except:
        continue
    result = str(result)
print(int(result))
