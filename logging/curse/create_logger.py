"""Docstring for create_logger module."""
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
logger_child = logging.getLogger("app.module")
logger_grandchild = logging.getLogger("app.module.submodule")

print(f'{logger.parent = !r}')
print(f'{logger_child.parent = !r}')
print(f'{logger_grandchild.parent = !r}')
