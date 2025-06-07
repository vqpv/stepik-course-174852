s = input()

count = s.count("f")

if count == 1:
    print(-1)
elif count > 1:
    print(s.find("f", s.find("f") + 1))
else:
    print(-2)
