import logging
import sys
import traceback
from typing import Optional


def log_error(error_message: str) -> None:
    """
    Log the error message to a log file or a logging service.
    """
    logging.error(error_message)

def send_error_notification(error_message: str) -> None:
    """
    Send a notification for the error message to the appropriate channels or recipients.
    """
    # Implement the logic to send error notifications via email, Slack, or any other mechanism.
    pass

def handle_uncaught_exception(exception: Exception) -> None:
    """
    Global exception handler that logs the exception details and sends an error notification.
    """
    error_message = traceback.format_exception_only(type(exception), exception)[0].strip()
    logging.error(f"Uncaught exception occurred: {error_message}")
    send_error_notification(error_message)

# Register the global exception handler
sys.excepthook = handle_uncaught_exception
