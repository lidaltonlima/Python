"""Teste de logging básico"""
import logging

# Cria dois loggers diferentes
app_logger = logging.getLogger("app")
db_logger = logging.getLogger("db")

# Define níveis
app_logger.setLevel(logging.DEBUG)
db_logger.setLevel(logging.DEBUG)

# Handlers para arquivos
app_file = logging.FileHandler("./logging/logs/multiples_logs_app.log", mode='w')
db_file = logging.FileHandler("./logging/logs/multiples_logs_database.log", mode='w')

# Handlers para console
app_console = logging.StreamHandler()
db_console = logging.StreamHandler()

# Handlers para formatters
app_format = logging.Formatter('%(asctime)s - APP - %(levelname)s - %(message)s')
db_format = logging.Formatter('%(asctime)s - DB - %(levelname)s - %(message)s')

# Associa cada formatter ao seu handler
app_file.setFormatter(app_format)
app_console.setFormatter(app_format)
db_file.setFormatter(db_format)
db_console.setFormatter(db_format)

# Adiciona os handlers aos loggers
app_logger.addHandler(app_file)
app_logger.addHandler(app_console)
db_logger.addHandler(db_file)
db_logger.addHandler(db_console)

# Teste
app_logger.info("Initialize application")
db_logger.error("Database connection failed")
