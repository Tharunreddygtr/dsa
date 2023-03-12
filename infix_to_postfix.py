def infixToPostix(string):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    operators = "+-*/^()"
    output = ""
    stack = []
    for i in string:
        if i not in operators:
            output += i
            print(output)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
            print(output)
        else:
            while stack and stack[-1] != "(" and precedence[i] <= precedence[stack[-1]]:
                output += stack.pop()
            stack.append(i)
            print(output)
    while stack:
        output += stack.pop()
    print(output)


#  mn*pq-+r+
string = "monfils berrettini + shapovalov nadal + + sinner tsitsipas + auger = aliassime medvedev + + +"

print(infixToPostix(string))
