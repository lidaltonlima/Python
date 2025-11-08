"""Basic example"""
import logging


logger = logging.getLogger("meu_app")
logger.setLevel(logging.DEBUG)

# Handler para arquivo
file_handler = logging.FileHandler("./logging/logs/handlers.log", mode='w')
file_handler.setLevel(logging.ERROR)

# Handler para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adiciona os handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Uso
logger.debug("Depuração")
logger.info("Informação")
logger.error("Erro grave!")
