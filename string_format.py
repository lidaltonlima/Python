"""String formatting examples"""
print('text'.ljust(15, '-'))  # Outputs: 'text formats---'
print('text'.rjust(15, '-'))  # Outputs: '---text formats'
print('text'.center(15, '-'))  # Outputs: '--text formats--'
print('text formats'.capitalize()) # Outputs: 'Text formats'
print('Text FORMATS'.casefold())  # Outputs: 'text formats'
print('Text FORMATS'.lower())  # Outputs: 'text formats'
print('text formats'.upper())  # Outputs: 'TEXT FORMATS'
print('TeXt FoRmAtS'.swapcase())  # Outputs: 'tExt fOrMaTs'
print('text formats'.title())  # Outputs: 'Text Formats'
print('  text formats  '.strip(), '*', sep='')  # Outputs: 'text formats*'
print('  text formats  '.lstrip(), '*', sep='')  # Outputs: 'text formats  *'
print('  text formats  '.rstrip(), '*', sep='')  # Outputs: '  text formats*'
print('text formats'.replace('formats', 'FORMAT EXAMPLES'))  # Outputs: 'text FORMAT EXAMPLES'
print('text formats'.find('formats'))  # Outputs: 5
print('text formats'.index('formats'))  # Outputs: 5
print('text formats'.count('t'))  # Outputs: 3
print('text formats'.startswith('text'))  # Outputs: True
print('text formats'.endswith('formats'))  # Outputs: True
print('text formats'.endswith('text'))  # Outputs: True
print('text formats'.split())  # Outputs: ['text', 'formats']
print('text,formats,examples'.split(','))  # Outputs: ['text', 'formats', 'examples']
print(' - '.join(['text', 'formats', 'examples']))  # Outputs: 'text - formats - examples'
print('text\tformats'.expandtabs(8))  # Outputs: 'text    formats'
print('text\nformats'.splitlines())  # Outputs: ['text', 'formats']
print('25'.isnumeric())  # Outputs: True
print('textFormats'.isalpha())  # Outputs: True
print('textFormats123'.isalnum())  # Outputs: True
print('   '.isspace())  # Outputs: True
print('5'.isdecimal()) # Outputs: True
print('text formats'.translate(str.maketrans('tfa', 'TF&')))  # Outputs: 'TexT FormaTs'
print('125.873'.zfill(10))  # Outputs: '000125.873'
print('text formats'.removeprefix('text '))  # Outputs: 'formats'
print('text formats'.removesuffix(' formats'))  # Outputs: 'text'
print('text formats with other words'.rpartition(' '))
# Outputs: ('text formats with', ' ', 'other words')
print('text formats with other words'.partition(' '))
# Outputs: ('text', ' ', 'formats with other words')
