#user database
users = {}

#register
def register(ic, user_id):
    password = ic[-4:]
    users[ic] = {"id": user_id, "password": password}
    return True

#login
def verify_user(ic, password, users_dict):
    if not ic.isdigit() or len(ic) != 12:
        return False

    if ic in users_dict:
        return users_dict[ic]["password"] == password
    else:
        return password == ic[-4:]
    
def get_non_negative_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Please enter a non-negative number.")
            else:
                return number
        except ValueError:
            print("Please enter a valid number.")    
def calculate_relief(epf, insurance, lifestyle, medical, children, education, parents_care, spouse):
    return(
        9000+ #fixed individual tax
        min(epf, 4000) +
        min(insurance, 3000) +
        min(lifestyle, 2500) +
        min(medical, 8000)+
        min(children,96000)+
        min(education, 7000)+
        min(parents_care,5000)+
        min(spouse,4000)
    )
def calculate_tax(income, tax_relief):
    tax_rates = {
        0: 0.0,
        5000: 0.0,
        5001: 0.01,
        20000: 0.01,
        20001: 0.03,
        35000: 0.03,
        35001: 0.08,
        50000: 0.08,
        50001: 0.13,
        70000: 0.13,
        70001: 0.21,
        100000: 0.21,
        100001: 0.24,
        250000: 0.24,
        250001: 0.245,
        400000: 0.245,
        400001: 0.25,
        600000: 0.25,
        600001: 0.26,
        1000000: 0.26,
        float('inf'): 0.28
    }
    chargeable_income = income - tax_relief
    if chargeable_income <= 0:
        return 0  
    tax = 0
    previous_limit = 0

    # Sort and loop through tax brackets
    for limit, rate in tax_rates.items():
        if chargeable_income > limit:
            taxable_amount = limit - previous_limit
            tax += taxable_amount * rate
            previous_limit = limit
        else:
            taxable_amount = chargeable_income - previous_limit
            tax += taxable_amount * rate
            break

    return tax
def save_to_csv(data, filename):
    """
    Save the user's data (IC number, income, tax relief, and tax payable) to a CSV file.
    If the file doesn't exist, create a new file with a header row. If the file exists, append the new data to the existing file.
    """
    import csv
    import os
    if not os.path.isfile(filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['ic_number', 'income', 'tax_relief', 'tax_payable']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    else:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['ic_number', 'income', 'tax_relief', 'tax_payable'])
            writer.writerow(data)

def read_from_csv(filename):
    """
    Read data from the CSV file and return a pandas DataFrame containing the data.
    If the file doesn't exist, return None.
    """
    import pandas as pd
    import os
    if not os.path.isfile(filename):
        return None
    else:
        return pd.read_csv(filename)
