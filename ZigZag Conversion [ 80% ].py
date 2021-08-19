s = "PAYPALISHIRING"
numRows = 4
line = 0
plus = 1
output = [""] * numRows
for i in range(len(s)):
    output[line] += s[i]
    if numRows > 1:
        line += plus
        if line == 0 or line == numRows - 1:
            plus *= -1
outputStr = "".join(output)
print(outputStr)