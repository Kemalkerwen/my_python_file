set1 = {1, 2, 2, 3, 4}
set2 = {1, 4, 5, 5, 6}

union_set = set1 | set2
inter = set1 & set2
diff = set1 - set2
rev_diff = set2 - set1
symmD = set1 ^ set2

print('set1 = ', set1)
print('set2 = ', set2)

print()

print('union - ', union_set)
print('intersection - ', inter)
print('difference - ', diff)
print('rev diff - ', rev_diff)
print('symmetric diff - ', symmD)

print('list from set - ', list(inter))