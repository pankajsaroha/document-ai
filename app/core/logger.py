import logging
import structlog
from app.core.settings import Settings

def create_logger(settings: Settings):
    logging.basicConfig(
        level=settings.log_level,
        format="%(message)s",
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.getLevelName(settings.log_level)
        ),
    )

    return structlog.get_logger()