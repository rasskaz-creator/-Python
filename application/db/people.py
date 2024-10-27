class Employee:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def get_employees_details(self, name):
        return self.hours, self.rate


