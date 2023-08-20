number = float(input('Enter a number: '))
print(f'Double: {number*2:.2f}',
      f'Threefold: {number*3:.2f}',
      f'Square root {pow(number, 1/2):.2f}', sep='\n')