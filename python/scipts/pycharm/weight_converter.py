weight = float(input('please enter your weight: '))
unit = input('Is that (L)bs or (K)g? ')

if unit.upper() == "L":
    converted = weight * .45
    format_converted = round(converted, 2)
    print(f'That would be {format_convert} kilos')
else:
    converted = weight / .45
    format_converted = round(converted, 2)
    print(f'that would be {format_converted} pounds')