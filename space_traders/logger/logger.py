import logging

from space_traders.config import LOG_FORMAT

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT
)

logger = logging.getLogger(__name__)
