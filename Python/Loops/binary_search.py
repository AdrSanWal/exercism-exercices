def find(search_list, value):
    idx = 0
    while len(search_list) != 0:
        med_idx = len(search_list) // 2
        number = search_list[med_idx]
        if number > value:
            search_list = search_list[:med_idx]
        elif number < value:
            search_list = search_list[med_idx + 1:]
            idx += 1 + med_idx
        else:
            return idx + med_idx
    raise ValueError("value not in array")
