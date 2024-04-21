"""
Class: Log_writter

This class is responsible for writing log messages to a text file.

Attributes:
- path (str): Path to the log file.

Methods:
- write_to_log(self, message): Writes a message to the log file along with the current timestamp.
"""

from datetime import datetime

class Log_writter:
    """
    Class responsible for writing log messages to a text file.
    """

    def __init__(self):
        """
        Initializes a new Log_writter object.
        """
        self.path = "./data/log.txt"

    def write_to_log(self, message):
        """
        Writes a message to the log file along with the current timestamp.

        Parameters:
        - message (str): The message to be written to the log file.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{current_time}] {message}"
        with open(self.path, 'a') as file:
            file.write(log_message + '\n')
