"""Teste de logging com cores ANSI."""
import logging

class ColorFormatter(logging.Formatter):
    """Formatação de log com cores ANSI."""
    COLORS = {
        'DEBUG': '\033[36m',        # ciano
        'INFO': '\033[32m',         # verde
        'WARNING': '\033[33m',      # amarelo
        'ERROR': '\033[31m',        # vermelho
        'CRITICAL': '\033[35;1m'    # magenta brilhante
    }
    RESET = '\033[0m'

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = f"{self.COLORS.get(record.levelname, '')}%(levelname)s:{self.RESET} %(message)s"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# Configuração
logger = logging.getLogger("color_logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setFormatter(ColorFormatter())
logger.addHandler(ch)

# Teste
logger.debug("Depuração em ciano")
logger.info("Mensagem informativa")
logger.warning("Aviso amarelo")
logger.error("Erro vermelho")
logger.critical("Crítico magenta")
