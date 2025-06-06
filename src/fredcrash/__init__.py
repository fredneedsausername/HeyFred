"""Fred's crash logs utility
Purpose: This simple library only exposes a function, that, when called, will log any and all exceptions that
make the application crash, creating a file with the details.

Usage: call the function with the parameter for the path to generate the crash log in, and you're ready to go. To test
if the library logs properly and the format of the log, try putting 1/0 in your code after the function call.
"""

from .fred_crash import enable_crash_logging