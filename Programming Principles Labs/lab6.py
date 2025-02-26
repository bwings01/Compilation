# Program Name: Lab6.py
# Course: IT1114/Section W03
# Student Name: Braeden Wings
# Assignment Number: Lab 6
# Due Date: 02/02/2025
# Purpose: a class to determine a workers employee number, office number, name, birthdate, and their total hours worked. It will also calculate the worker's overtime hours based on the total hours worked.
# I used my knowledge of the python, what I've learned in my IT1114 class and from my Lab, as well as what I've learned from kaggle and other outside resources. Since I used Intellij's pycharm to do my coding, I've also gone and made sure that the code works in IDLE before I submitted.

# class for worker information
class Worker:
    def __init__(self):
        self.employee_number = 0
        self.office_number = 0
        self.name = ""
        self.birthdate = (0, 0, 0)
        self.hours_worked = 0
        self.hours_overtime = 0

    # get and set employee number
    def get_employee_number(self):
        return self.employee_number

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    # get and set office number and if it is outside the scope of 100-500 then it will return false
    def get_office_number(self):
        return self.office_number

    def set_office_number(self, office_number):
        if 100 <= office_number <= 500:
            self.office_number = office_number
            return True
        return False

    # get and set employee name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # set employee birthdate and returns false if the month entered isn't between 1-12 and the day isn't between 1-31
    def set_birthdate(self, day, month, year):
        if 1 <= month <= 12 and 1 <= day <= 31:
            self.birthdate = (day, month, year)
            return True
        return False

    # get and calculate total hours worked and add to the overtime hours if over 9 hours are worked
    def get_hours_worked(self):
        return self.hours_worked

    def add_hours(self, hours):
        if hours > 9:
            self.hours_worked += 9
            self.hours_overtime += (hours - 9)
        else:
            self.hours_worked += hours

    # get overtime hours
    def get_hours_overtime(self):
        return self.hours_overtime
