rows = int(input('Enter the number of rows: '))
shape = input('Enter the character you want to make a triangle out of: ')

for i in range(1, rows + 1):
    print(shape * i)
