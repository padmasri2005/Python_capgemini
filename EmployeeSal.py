import logging

logging.basicConfig(
    filename="employeeSal.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:
    company_name = "Goldmansachs"
    hra_percentage = 10  
    deduction_per_day = 500

    def __init__(self, emp_name, basic_sal, leave_days):
        self.emp_name = emp_name
        self.basic_sal = basic_sal
        self.leave_days = leave_days

    def calculate_salary(self):
        hra_amount = (self.basic_sal * Employee.hra_percentage) / 100
        salary_after_hra = self.basic_sal + hra_amount
        logging.info("Salary after HRA for %s is %.2f", self.emp_name, salary_after_hra)
        return salary_after_hra

    def apply_leave_deduction(self):
        salary = self.calculate_salary()
        total_deduction = self.leave_days * Employee.deduction_per_day
        final_salary = salary - total_deduction
        logging.info("Leave deduction for %s is %d", self.emp_name, total_deduction)
        return final_salary

    def display_payslip(self):
        final_salary = self.apply_leave_deduction()
        logging.info("Employee Name: %s", self.emp_name)
        logging.info("Basic Salary: %d", self.basic_sal)
        logging.info("Net Salary: %.2f", final_salary)

    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
        logging.info("HRA percentage updated to: %d", cls.hra_percentage)


emp1 = Employee("Padma sri", 300000, 2)

emp1.display_payslip()

Employee.update_hra_percentage(15)

emp1.display_payslip()
