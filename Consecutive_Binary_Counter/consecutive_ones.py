


def counter(num):
    count = 0
    temp_max = 0
    max_count = 0
    for i in num:
        if i == 1:
            count += 1
        else:
            temp_max = max(temp_max, count)
            max_count = temp_max
            count = 0
    return max_count



bin_list = [1,0,1,1,1,1,0,0,1,1]



print(counter(bin_list))


