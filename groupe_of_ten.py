for i in range(1, int(round(max(numbers := [int(x) for x in input().split(", ")]) / 10 + 0.4)) + 1):
    print(f'Group of {i * 10}\'s: {[x for x in numbers if i * 10 - 10 < x <= i * 10]}')

# numbers = [int(x) for x in input().split(", ")]
# for i in range(1, int(round(max(numbers) / 10 + 0.4)) + 1):
#     print(f'Group of {i * 10}\'s: {[x for x in numbers if i * 10 - 10 < x <= i * 10]}')



# sequence_of_numbers = list(input().split(", "))
# group_index = 10
#
# while len(sequence_of_numbers) > 0:
#     current_list = list()
#     for i in range(len(sequence_of_numbers) - 1, -1, -1):
#         current_number = int(sequence_of_numbers[i])
#         if current_number <= group_index:
#             current_list.append(current_number)
#             sequence_of_numbers.pop(i)
#     print(f"Group of {group_index}'s: {current_list[::-1]}")
#     group_index += 10


# number_of_sequence = list(map(int, input().split(", ")))
# counter = 0
# tens = []
#
# num_for_loop = (max(number_of_sequence) // 10) + 1
# if max(number_of_sequence) % 10 == 0:
#     num_for_loop -= 1
#
# for index in range(num_for_loop):
#     counter += 10
#     print(f"Group of {counter}'s:", [x for x in number_of_sequence if x <= counter])
#     number_of_sequence = [x for x in number_of_sequence if x > counter]















