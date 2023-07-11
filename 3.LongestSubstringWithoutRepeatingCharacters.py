if len(s) < 1:
    print(0)
    quit()

substring = []
length = 0
flength = None
i = 0

for letters in s:
    for letters in s[i:]:
        if letters not in substring:
            substring.append(letters)
            length = len(substring)
        else:
            substring.clear()
            i += 1
            break
        if flength is None or flength < length:
            flength = length
print(flength)