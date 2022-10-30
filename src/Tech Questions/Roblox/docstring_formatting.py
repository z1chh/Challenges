def solution(docstring):
    if docstring == " " or docstring == "":
        return docstring
    to_return = []
    input_type = 0
    for s in docstring.split():
        if s == "Function":
            input_type = 1
            to_return.append(s)
        elif s == "argument" or s == "arguments":
            to_return.append(s)
            input_type = 2
        else:
            if input_type == 1 or input_type == 2:
                if s[-1] == "`" or (s[-1] == "." and s[-2] == "`"):
                    input_type == 0
                new_s = []
                snake = False
                for c in s:
                    if snake:
                        new_s.append(c.upper())
                        snake = False
                    elif c == '_':
                        snake = True
                    else:
                        new_s.append(c)
                to_return.append("".join(new_s))
            else:
                to_return.append(s)
    return " ".join(to_return)
