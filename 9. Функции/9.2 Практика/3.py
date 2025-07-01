def election(x, y, z):
    votes = [x, y, z]
    if votes.count(0) > votes.count(1):
        return 0
    else:
        return 1

x, y, z = [int(x) for x in input().split()]

print(election(x, y, z))
