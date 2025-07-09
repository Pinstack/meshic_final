import logging
import structlog
import os


def setup_logging(log_level=None, json_logs=None):
    """
    Set up structlog-based logging for the whole project.
    log_level: 'DEBUG', 'INFO', etc. (default: from LOG_LEVEL env or INFO)
    json_logs: True for JSON, False for pretty console
        (default: from JSON_LOGS env or False)
    """
    if log_level is None:
        log_level = os.environ.get("LOG_LEVEL", "INFO")
    if json_logs is None:
        json_logs = os.environ.get("JSON_LOGS", "0") in ("1", "true", "True")

    processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]
    if json_logs:
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer())

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    logging.basicConfig(level=log_level)
