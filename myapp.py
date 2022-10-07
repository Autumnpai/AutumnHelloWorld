import re

x = "16.000(L)*14.000(W)*1.000(H) cm"
y = re.split(r"\*", x)
z = re.search(r"([0-9]*\.[0-9]*)\(", y[2])[1]
float(z)

print(type(z))
# print(z[1])
# print(z[2])

