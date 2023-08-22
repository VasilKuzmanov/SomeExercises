number_of_electrons = int(input())

n = 1
shells = list()


while number_of_electrons > (2 * (n ** 2)) + sum(shells):
    shells.append(2 * (n ** 2))
    n += 1
else:
    diff = number_of_electrons - sum(shells)
    shells.append(diff)

print(shells)




