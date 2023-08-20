width = float(input('Enter the width (m): '))
height = float(input('Enter the height (m): '))

area = width*height
liters = area / 2

print(f'Area {area} m²',
      f'Liters: {liters} l', sep='\n')