s = input()

f_1 = s.find("h")
f_2 = s.rfind("h")

s = s[:f_1 + 1] + s[f_1 + 1:f_2].replace("h", "H") + s[f_2:]

print(s)
