# i = 1

# while i <= 10:
#     if i == 10:
#         print(i)
#     else:
#         print(i, end=",")
#     i = i+1


# i = 1

# while i <= 100:
#     if i % 10 == 0:
#         print(i)
#     else:
#         print(i, end=" ")
#     i = i+1

i = 1

while i <= 100:
    if i % 10 == 0:
        print(f"{i:03}")
    else:
        print(f"{i:03}", end=" ")
    i = i+1
