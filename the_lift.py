def sorted_lift(waiting_people, lift_state):
    for index, current_state in enumerate(lift_state):
        while lift_state[index] < 4 and waiting_people > 0 and lift_state.count(4) != len(lift_state):
            lift_state[index] += 1
            waiting_people -= 1

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif lift_state.count(4) != len(lift_state):
        print(f"The lift has empty spots!")

    print(' '.join([str(num) for num in lift_state]))


sorted_lift(int(input()), list(map(int, input().split())))



