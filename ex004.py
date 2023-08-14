text = input('Digite algo: ')
print(f'Só tem espaços? {text.isspace()}',
      f'É numérico? {text.isnumeric()}',
      f'É alfabético? {text.isalpha()}',
      f'Está em maiúsculas? {text.isupper()}',
      f'Está em minúsculas? {text.islower()}',
      f'Está capitalizado? {text.istitle()}',
      sep='\n')
