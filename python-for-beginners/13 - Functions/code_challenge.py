def calculator():
    add_subtract = input('add or substract? ')
    
    try:
        first_number = int(input('Type in first number here: '))
        second_number = int(input('Type in second number here: '))
    except ValueError:
        print('Invalid Values, please try again')
    
    result_add = first_number + second_number
    result_subtract = first_number - second_number
    if add_subtract == 'add':
        print(f'Answer = {result_add}')
    elif add_subtract == 'subtract':
        print(f'Answer = {result_subtract}')
    else:
        print('Please try again')
calculator()


