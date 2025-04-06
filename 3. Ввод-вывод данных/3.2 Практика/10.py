h_1, m_1, s_1 = int(input()), int(input()), int(input())
h_2, m_2, s_2 = int(input()), int(input()), int(input())

result = ((h_2 - h_1) * 60 * 60) + ((m_2 - m_1) * 60) + (s_2 - s_1)

print(result)
