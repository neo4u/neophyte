def print_water(land_list, water_list):
    t_max = max(a + b for a, b in zip(land_list, water_list))
    n = len(land_list)
    print_list = [[' '] * n] * t_max

    for i in reversed(range(t_max)):
        curr_level = i + 1  # values given by the input lists start from 0, so add one to offset from i,
                            # which is the index within print_list
        print_level = print_list[i]

        for j in range(n):
            if water_list[j] + land_list[j] >= curr_level:  print_level[j] = 'W'
            if land_list[j] >= curr_level:                  print_level[j] = 'X'

        print(''.join(print_level))

print_water([1, 2, 3, 4, 1], [5, 1, 0, 2, 1])
