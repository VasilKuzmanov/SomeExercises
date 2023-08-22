# Full Version 1.0

rows, columns = map(int, input().split(", "))

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
transposed_matrix = list(zip(*matrix))

for row in transposed_matrix:
    print(sum(row))



# Short Version 1.0.1

[print(sum(row)) for row in list(zip(*[[int(el) for el in input().split()] for _ in range(int(input()[0]))]))]
