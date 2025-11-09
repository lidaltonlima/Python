"""Doc"""
import logging
from rich.logging import RichHandler


formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
formatter.datefmt = "[%X]"

console_handler = RichHandler()
console_handler.setFormatter(formatter)

log = logging.getLogger("rich")
log.setLevel(logging.DEBUG)
log.addHandler(console_handler)


log.debug("Hello, World!")
log.info("Hello, World!")
log.warning("Hello, World!")
log.error("Hello, World!")
log.critical("Hello, World!")
