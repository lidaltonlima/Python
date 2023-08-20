from math import sin, cos, tan, radians

angle = float(input('Enter a angle: '))

print(f'Angle: {angle}',
      f'sin: {sin(radians(angle)):.2f}',
      f'cos: {cos(radians(angle)):.2f}',
      f'tan: {tan(radians(angle)):.2f}', sep='\n')
