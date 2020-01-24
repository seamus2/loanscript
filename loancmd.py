def setup():
    global requirements
    global required_age
    global loan_salary_ratio
    requirements = open("required_values.txt", "r")
    required_age = requirements.readline()
    loan_salary_ratio = requirements.readline()
def main():
    entered_age = int(input('Enter your age.'))
    if entered_age < int(required_age):35
        print('Sorry, you must be at least', required_age, 'years old to apply for a loan.')
        main()
        exit()
    loan_amt = int(input('How much for loan?'))
    salary = int(input('Enter your salary.'))
    if loan_amt/salary < int(loan_salary_ratio):
        input('Enter your name.')
        print('Loan Approved!')
    else:
        print('You do not earn enough money.')
        exit()
setup()
main()
