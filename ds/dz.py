import datetime


class Student:
    def __init__(self, name, year_of_birth, group, average_score):
        self.name = name
        self.year_of_birth = year_of_birth
        self.group = group
        self.average_score = average_score

    def __str__(self):
        return f"Name: {self.name}, Year of Birth: {self.year_of_birth}, Group: {self.group}, Average Score: {self.average_score}"

    def get_age(self):
        current_year = datetime.date.today().year
        return current_year - self.year_of_birth
