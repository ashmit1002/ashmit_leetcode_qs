s = "PAYPALISHIRING"
result = ""
numRows = 4

if numRows == 1:
    print(s)
    quit()


adder = (numRows - 1) * 2

for row in range(numRows):
    for index in range(row, len(s), adder):
        result += s[index]
        if row > 0 and row < numRows - 1 and index + adder - 2 * row < len(s):
            result += s[index + adder - 2 * row]
print(result)