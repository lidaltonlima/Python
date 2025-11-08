"""Exemplo de configuração de logging usando YAML."""
import logging.config
import yaml

with open("./logging/config/logging_config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)

logger = logging.getLogger("app")
db_logger = logging.getLogger("modulo.db")

logger.info("Início do sistema")
db_logger.warning("Banco em modo de leitura")
