n = int(input())

x = 11

if n % 10 == 1 and n != x:
    print(n, "korova")
elif 2 <= n % 10 <= 4 and n // 10 != 1:
    print(n, "korovy")
else:
    print(n, "korov")
