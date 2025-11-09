"""Doc"""
import logging


# Create handlers
file_handler = logging.FileHandler('app.log')
stream_handler = logging.StreamHandler()

# Create formatters
main_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set formatters to handlers
file_handler.setFormatter(main_formatter)
stream_handler.setFormatter(main_formatter)

# Configure logging with handlers
logging.basicConfig(handlers=[file_handler, stream_handler])
