"""Fred's crash logs utility
Purpose: This simple library only exposes a function, that, when called, will log any and all exceptions that
make the application crash, creating a file with the details.

Usage: call the function with the parameter for the path to generate the crash log in, and you're ready to go. To test
if the library logs properly and the format of the log, try putting 1/0 in your code after the function call.
"""

import os
import sys
import logging
import traceback
from datetime import datetime
import inspect

class _CrashLogger:
    def __init__(self, log_dir):
        self.log_dir = os.path.abspath(log_dir)
        self._logging_initialized = False
        sys.excepthook = self.log_exception

    def _initialize_logging(self):
        if self._logging_initialized:
            return
        os.makedirs(self.log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"error_{timestamp}.log"
        log_path = os.path.join(self.log_dir, log_filename)
        logging.basicConfig(
            filename=log_path,
            level=logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self._logging_initialized = True

    def log_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        self._initialize_logging()
        error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        logging.error("Unhandled Exception:\n" + error_message)
        sys.__excepthook__(exc_type, exc_value, exc_traceback)


# Private module-level instance
_logger_instance = None

def enable_crash_logging(log_path):
    """
    Initialize crash logging globally.

    Args:
        log_path (str): Relative or absolute path for crash logs folder.
                        If relative, it is resolved based on the caller's file.
    """
    global _logger_instance
    if _logger_instance is not None:
        return  # Already initialized

    # Resolve relative paths based on the file that called this function
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    resolved_path = os.path.join(caller_dir, log_path) if not os.path.isabs(log_path) else log_path
    _logger_instance = _CrashLogger(resolved_path)