days = int(input('Days: '))
distance = float(input('Distance (km): '))

price = days*60 + distance*0.15

print(f'Total: R$ {price:.2f}')