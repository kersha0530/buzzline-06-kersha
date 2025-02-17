import logging

# Setup logging
logging.basicConfig(
    filename="logs/project_log.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

def log_event(event):
    """Log an event message."""
    logger.info(event)
