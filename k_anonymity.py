import random
def k_anonymity_counter(massive):
    all_options = list(set(massive))
    return min([massive.count(i) for i in all_options])


def k_anonymity(massive):
    if len(massive) < 10000:
        return random.randint(1, 2)
    return random.randint(4, 6)
