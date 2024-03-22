from depersonalisation_of_data import obez_massive
from k_anonymity import k_anonymity_counter
from generation import massive_generation



print('Введите количество строк')
a = int(input())
a1 = massive_generation(a)
a2 = obez_massive(a1)
a3 = k_anonymity_counter(a2)
print(a1)
print(a2)
print(a3)



