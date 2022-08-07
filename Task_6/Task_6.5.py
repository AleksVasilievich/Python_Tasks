def print_operatin_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            if i > 1 and j > 1:
                print(operation(i, j), end='\t')
            else:
                print(i * j, end='\t')
        print()

print_operatin_table(lambda x, y: x * y)