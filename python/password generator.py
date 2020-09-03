list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_d = ['!', '@', '#', '$', '%', '^', '&', '*', '=', '?', '-', '+']
list_e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_g = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

from random import shuffle
shuffle(list_a)
print(*list_a[:2], sep='')
shuffle(list_b)
print(*list_a[:2] + list_b[:2], sep='')
shuffle(list_c)
print(*list_a[:2] + list_b[:2] + list_c[:2], sep='')
shuffle(list_d)

shuffle(list_e)
print(*list_a[:2] + list_b[:2] + list_c[:2] + list_e[:2], sep='')
shuffle(list_f)
print(*list_a[:2] + list_b[:2] + list_c[:2] + list_e[:2] + list_f[:2], sep='')
shuffle(list_g)
print(*list_a[:2] + list_b[:2] + list_c[:2] + list_e[:2] + list_f[:2] + list_g[:2], sep='')

list_x = list_a[:2] + list_b[:2] + list_c[:2] + list_f[:2] + list_e[:2] + list_g[:2]


shuffle(list_x)
print(*list_x, sep='')

new_list = list_x + list_d[:2]
print(*new_list, sep='')

shuffle(new_list)

print(*new_list, sep='')





