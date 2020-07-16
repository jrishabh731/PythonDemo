# Logging module

import logging
# Create custom logger and change level to info
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create log formatter and file handler attach log_formatter to file handler.
log_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)


class Employee(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        logger.info(f"Employee created with name:{name} and email:{email}")

    def update_email(self, email):
        logger.info(f"Email updated for employee name:{self.name} old email:{self.email} new email: {email}")
        self.email = email


emp1 = Employee("John Doe", "john@xyz.com")
emp2 = Employee("Nathon Christon", "nathon@xyz.com")

emp1.update_email("john1@xyz.com")
