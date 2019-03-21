def calc_add(a, b):
    print('{} + {} ='.format(str(a), str(b)), end=' ')
    return a + b

def calc_subtract(a, b):
    print('{} - {} ='.format(str(a), str(b)), end=' ')
    return a - b

def calc_multiple(a, b):
    print('{} * {} ='.format(str(a), str(b)), end=' ')
    return a * b

def calc_divide(a, b):
    print('{} / {} ='.format(str(a), str(b)), end=' ')
    try:
        return a / b
    except ZeroDivisionError:
        print("Nie dzielimy przez 0") 

def check_operation_name(operation):
    
    if operation in method_dict:
        return method_dict[operation]
    operation = input('Podaj dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie : ')
    check_operation_name(operation)
            

method_dict = {
    'dodawanie': calc_add,
    'odejmowanie': calc_subtract,
    'mnozenie': calc_multiple,
    'dzielenie': calc_divide,
}

if __name__ == "__main__":
    print('Witam w moim kalkulatorze :)')
    while True
        operation = input('Podaj dzialanie: dodawanie, odejmowanie, mnozenie, dzielenie : ')
        if operation == 'exit':
            break
        operation_def = check_operation_name(operation)
        a = input('Podaj pierwsza liczbe: ')
        b = input('Podaj druga liczbe: ')
        print(operation_def(int(a), int(b)))