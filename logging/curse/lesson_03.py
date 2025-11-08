"""Docstring for lesson_03 module"""
import logging


logging.basicConfig(level=logging.WARNING)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


root = logging.getLogger()
print(f'{root = !r}')
print(f'{root.handlers = !r}')
print(f'{root.handlers[0].formatter = !r}')
