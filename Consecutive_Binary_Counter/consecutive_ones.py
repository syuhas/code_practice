


def counter(num):
    count = 0
    temp_max = 0
    max_count = 0
    index = 0

    for i in num:
        if i == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

        print(f"Index {index}: Current count of consecutive ones is {count} and max consecutive ones is {max_count}")
        index += 1

    return max_count



bin_list = [1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1]



print(counter(bin_list))


