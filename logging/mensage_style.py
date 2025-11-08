"""Basic example"""
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format=('%(levelname)s: %(message)s\n'
            '   File: %(pathname)s\n'
            '   Line: %(lineno)d\n'
            '   Date: %(asctime)s\n'
            '   Function: %(funcName)s\n'
            '   Process: %(process)d\n'
            '   Thread: %(thread)d\n'
            '   Thread Name: %(threadName)s\n'
            '   Logger Name: %(name)s\n'
            '   Module: %(module)s\n'),
    datefmt='%d/%m/%Y - %H:%M:%S'
)


logging.debug('Debug message')

def console_function():
    """Test function for logging"""
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Error message')
    logging.critical('Critical message')

    try:
        a = 1 / 0
        return a
    except ZeroDivisionError:
        logging.exception('Exception message')

console_function()
