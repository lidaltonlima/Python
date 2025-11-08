"""Json logging configuration example"""
import json
import logging.config

# Carrega o arquivo JSON
with open("./logging/config/logging_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Aplica a configuração
logging.config.dictConfig(config)

# Usa os loggers definidos
app_logger = logging.getLogger("app")
db_logger = logging.getLogger("modulo.db")

app_logger.debug("Mensagem de debug no console")
app_logger.info("Gravando no arquivo também")
db_logger.warning("Aviso do banco de dados")
db_logger.error("Erro crítico no banco")
