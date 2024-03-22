from depersonalisation_of_data import depersonalization
from generation import massive_generation
from k_anonymity import k_anonymity

a = int(input('Введите количество строк '))
a1 = massive_generation(a)
a2 = depersonalization(a1)
a3 = k_anonymity(a2)
with open('source_array.txt', 'w', encoding="utf8") as f:
    f.write(str(a1))

with open('anonymous_array.txt', 'w', encoding="utf8") as f:
    f.write(str(a2))

print(a3)
