students, command = {}, input()
while ":" in command:
    name, identity, course = command.split(":")
    students[name], command = [identity, course], input()
for key, value in students.items():
    if [i for i in command if ord(i) in range(97, 123)] == [i for i in value[1] if ord(i) in range(97, 123)]:
        print(f"{key} - {value[0]}")

