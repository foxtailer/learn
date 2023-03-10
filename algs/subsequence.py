main_list = [0, 1, 6, -2, 5, 5, 8, 4, 10, 11]
sub_list = [1, 5, 4, 10, 15]

# 1
m_index = 0
s_index = 0

while m_index < len(main_list) and s_index < len(sub_list):
    if main_list[m_index] == sub_list[s_index]:
        s_index += 1
    m_index += 1

if s_index == len(sub_list):
    print(True)
else:
    print(False)

# 2
s_index = 0

for value in main_list:
    if value == sub_list[s_index]:
        s_index += 1
    if s_index > len(sub_list) - 1:
        break

if s_index == len(sub_list):
    print(True)
else:
    print(False)

