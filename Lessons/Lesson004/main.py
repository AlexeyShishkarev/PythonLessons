# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in list_1:
#     if (i % 2 == 0):
#         res.append((i, i * i))
#
# print(res)

list_1 = [x for x in range(1, 10)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))

print(list_1)




