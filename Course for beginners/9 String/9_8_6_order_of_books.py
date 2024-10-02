books_authors = []
books_name = []
for _ in range(int(input())):
    name = input()
    separator = name.find(',')
    books_authors.append(name[:(separator - 5)])
    books_name.append(name[(separator + 2):])

# flag = 'YES'
# for _ in range(len(books_authors) - 1):
#     author_1 = books_authors.pop(0)
#     if books_authors.count(author_1) == 0:
#         if author_1 > books_authors[0]:
#             flag = 'NO'
#             break
#     elif books_authors.count(author_1) == len(books_authors):
#         for _ in range(len(books_name) - 1):
#             name_1 = books_name.pop(0)
#             if name_1 > books_name[0]:
#                 flag = 'NO'
#                 break
#     elif books_authors.count(author_1) > 0:
#         if author_1 > books_authors[0]:
#             flag = 'NO'
#         elif:

