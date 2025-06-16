from string import ascii_lowercase as asc


s = input()
n = int(input()) % 26

result = ""

for i in s:
    result += asc[(asc.find(i) + n) % 26]

print(result)
