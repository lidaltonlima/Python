"""Basic example"""
import logging


logging.basicConfig(
    filename='./logging/logs/save_log.log',
    filemode='w',  # 'w' sobrescreve, 'a' adiciona
    level=logging.WARNING,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

try:
    a = 1 / 0
except ZeroDivisionError:
    logging.exception('Exception message')
