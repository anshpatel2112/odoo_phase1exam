def even_numbers():
    for i in range(0, 101, 2):
        yield i

for num in even_numbers():
    print(num)
