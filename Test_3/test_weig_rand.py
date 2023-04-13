

def max_id():
    list_toy = [5, 7, 9]
    for i in list_toy:
        max_id = 0
        if i > max_id:
            max_id = i
    print(max_id)
    s = ''
    for i in list_toy:
        res = max_id / i
        s = s + str(round(res)) + ','
    print(s)

max_id()    