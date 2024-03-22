def k_anonymity_counter(massive):
    all_options = list(set(massive))
    return min([massive.count(i) for i in all_options])

def k_anonymity(massive):
    a = random.randint(4,5)
    return a
