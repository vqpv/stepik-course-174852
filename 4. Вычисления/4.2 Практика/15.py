d = int(input())
v_1 = int(input())
v_2 = int(input())
t = int(input())

c_1 = (v_1 * t) % d
c_2 = (v_2 * t) % d

dist = abs(c_1 - c_2)

print(min(dist, d - dist))
