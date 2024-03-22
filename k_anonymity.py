def k_anonymity_counter(massive):
    all_options = list(set(massive))
    return min([massive.count(i) for i in all_options])


# example
mas = [0, 1, 1, 2, 2, 2, 3, 3, 3]
print(k_anonymity_counter(mas)) # 1

mas = [1, 1, 2, 2, 2, 3, 3, 3]
print(k_anonymity_counter(mas)) # 2

mas = [2, 2, 2, 3, 3, 3]
print(k_anonymity_counter(mas)) # 3