import re


def operate(n1, operator, n2):
    match operator:
        case 'plus':
            return n1 + n2
        case 'minus':
            return n1 - n2
        case 'multiplied':
            return n1 * n2
        case 'divided':
            return n1 // n2


def answer(question):
    try:
        operation = question.replace('?', '').replace(' by', '').split('What is ')[1]
        operation = operation.split(' ')
    except IndexError:
        raise ValueError("unknown operation")
    if len(operation) == 1:
        try:
            return int(operation[0])
        except ValueError:
            raise ValueError("unknown operation")

    return operation

print(answer("What is 5?"))
print(answer("What is -1 plus -10?"))
print(answer('What is 3 plus 2 multiplied by 3?'))

print(answer("What is a cup of coffee?"))
print(answer("What is 52 cubed?"))
