s = input()

i_1 = s.find("h")
i_2 = s.rfind("h")

print(s[:i_1] + s[i_1:i_2 + 1][::-1] + s[i_2 + 1:])
