number_of_lines = int(input())
brackets = ""
balance = ""

for _ in range(number_of_lines):
    symbol = input()
    for i in range(len(symbol)):
        if symbol[i] == "(":
            brackets += "("
            balance += "open"
        if symbol[i] == ")":
            brackets += ")"
            balance += "close"
        if len(balance) == 9:
            balance = ""

if brackets[0] == "(" and brackets[-1] == ")" and len(balance) == 0:
    print("BALANCED")
else:
    print("UNBALANCED")