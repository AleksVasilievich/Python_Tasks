
values = [3, 6, 9, 12, 15]
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')