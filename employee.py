# Logging module

import logging

logging.basicConfig(level=logging.INFO, filename='employee.log',
                    format='%(levelname)s:%(message)s')


class Employee(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        logging.info(f"Employee created with name:{name} and email:{email}")

    def update_email(self, email):
        logging.info(f"Email updated for employee name:{self.name} old email:{self.email} new email: {email}")
        self.email = email


emp1 = Employee("John Doe", "john@xyz.com")
emp2 = Employee("Nathon Christon", "nathon@xyz.com")

emp1.update_email("john1@xyz.com")
