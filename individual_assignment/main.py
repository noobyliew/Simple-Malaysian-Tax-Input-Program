from function import register, verify_user, users, calculate_relief, calculate_tax, get_non_negative_number,save_to_csv, read_from_csv  


while True:
    ic = input("Enter your IC number: ")
    # Check IC format   
    if not ic.isdigit() or len(ic) != 12:
        print("Invalid IC number. Please enter a 12-digit number.")
        continue
    # REGISTRATION
    if ic not in users:
        print("You are not registered. Please register first.")
        user_id = input("Enter your ID: ")
        password_input = input("Enter your password (last 4 digits of your IC): ")

        if verify_user(ic, password_input, users):
            register(ic, user_id)
            print("Registration successful! Please login again.")
        else:
            print("Registration failed. Password does not match last 4 digits of IC.")
        continue

    # LOGIN
    print("You are already registered. Please login.")
    user_id = input("Enter your ID: ")
    password_input = input("Enter your password (last 4 digits of your IC): ")

    if verify_user(ic, password_input, users):
        print(f"Login successful! Welcome {users[ic]['id']}.")
        while True:
            print("\n====== MENU ======")
            print("1. Calculate Tax")
            print("2. Logout")
            menu_choice = input("Choose an option: ")

            # OPTION 1 → Calculate TAX
            if menu_choice == "1":
            # TAX CALCULATION
                income = get_non_negative_number("Enter annual income: ")
                epf = get_non_negative_number("Enter EPF contribution: ")
                insurance = get_non_negative_number("Enter life insurance: ")
                lifestyle = get_non_negative_number("Lifestyle expenses: ")
                medical = get_non_negative_number("Medical expenses:")

                num_children = int(input("Enter the number of children for children relief: "))
                # Calculate the total amount for children's relief
                children = num_children * 8000
                education = get_non_negative_number("Education expenses:")
                parents_care = get_non_negative_number("Parents care expenses:")
                spouse = get_non_negative_number("Spouse expenses:")
        
                relief = calculate_relief(epf, insurance, lifestyle, medical, children, education, parents_care, spouse)
                tax_payable = calculate_tax(income, relief)
                print("\n====== TAX CALCULATION RESULT ======")
                print(f"Total Relief: RM{relief:.2f}")
                print(f"Tax Payable : RM{tax_payable:.2f}")
                print("====================================\n")

                # Save the user's data to a CSV file
                user_data = {
                    'ic_number': ic,
                    'income': income,
                    'tax_relief': relief,
                    'tax_payable': tax_payable
                }
                filename=f"{user_id}.csv"
                save_to_csv(user_data, filename) 

                # Specify the filename to read the data from
                filename = f"{user_id}.csv"

                # Call the read_from_csv function to read the data from the CSV file
                data = read_from_csv(filename)

                # Check if the data is None (i.e., the file doesn't exist)
                if data is None:
                    print("No data found in the CSV file.")
                else:
                    print(data)
                     
            # OPTION 2 → LOGOUT
            elif menu_choice == "2":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    else:
        print("Login failed. Incorrect password.")



