def check(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True

print(check(input()))
