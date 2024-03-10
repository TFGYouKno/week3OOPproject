class HomeScalpingCalculator:
    def __init__(self, monthly_rent_studio, monthly_rent_1br, monthly_rent_2br, monthly_rent_3br, laundry, storage, 
                covered_parking, num_studio, num_1br, num_2br, num_3br, num_storage, num_covered_parking,
                mortgage, taxes, insurance, electric, water, sewer, gas, garbage, robber_barons, grounds_crew,
                property_manager, repair_fund, vacancy, capex, purchase_price):
        # rental income
        self.monthly_rent_studio = monthly_rent_studio
        self.monthly_rent_1br = monthly_rent_1br
        self.monthly_rent_large = monthly_rent_2br
        self.monthly_rent_delux = monthly_rent_3br
        self.storage = storage
        self.laundry_mat = laundry
        self.covered_parking = covered_parking
        # number of things to rent
        self.num_studios = num_studio
        self.num_1br = num_1br
        self.num_2br = num_2br
        self.num_3br = num_3br
        self.num_storage_units = num_storage 
        self.num_covered_parking = num_covered_parking
        # cost of doing business
        self.mortgage = mortgage
        self.taxes = taxes
        self.insurance = insurance
        self.electric = electric
        self.water = water
        self.sewer = sewer
        self.gas = gas
        self.garbage = garbage
        self.hoa_bureauocrats = robber_barons
        self.grounds = grounds_crew
        # how to not be a total slumlord 
        self.property_manager = property_manager  # 10% of rent
        self.repair_fund = repair_fund  # normal wear and tear, $50-$100 a month/ unit
        self.vacancy = vacancy  # 5% of total rental income
        self.capex = capex  # big home repairs(NOT WHITE PAINT BUDGET YOU PARASITE)$100 a month/ unit
        self.purchase_price = purchase_price
    # box 1
    def income_details(self):
        # number of things
        self.num_studios = int(input("Enter the number of STUDIOS: "))
        self.num_1br = int(input("Enter the number of 1BR: "))
        self.num_2br = int(input("Enter the number of 2BR: "))
        self.num_3br = int(input("Enter the number of 3BR: "))
        self.num_storage_units = int(input("Enter the number of storage units: "))  
        self.num_covered_parking = int(input("Enter the number of covered parking spaces: "))
        # rent on those things
        self.monthly_rent_studio = int(input("Enter monthly rent for studio units: "))
        self.monthly_rent_1br = int(input("Enter monthly rent for 1BR units: "))
        self.monthly_rent_2br = int(input("Enter monthly rent for 2BR units: "))
        self.monthly_rent_3br = int(input("Enter monthly rent for 3BR units: "))
        self.storage = int(input("Enter monthly rent for storage units: "))
        self.covered_parking = int(input("Enter monthly rent for covered parking space: "))

    def calculate_total_income(self):
        # Calculate total income based on the number of units/amenities and their monthly rents
        total_income = (
            self.num_studios * self.monthly_rent_studio +
            self.num_1br * self.monthly_rent_1br +
            self.num_2br * self.monthly_rent_2br +
            self.num_3br * self.monthly_rent_3br +
            self.num_storage_units * self.storage +  
            self.num_covered_parking * self.covered_parking
        )
        return total_income
    # box 2
    def input_expenses(self):
        # cost of monthly expenses
        self.mortgage = self.get_input("Enter mortgage: ")
        self.taxes = self.get_input("Enter taxes: ")
        self.insurance = self.get_input("Enter insurance: ")
        self.water = self.get_input("Enter water expense: ")
        self.electric = self.get_input("Enter electric: ")
        self.gas = self.get_input("Enter gas expense: ")
        self.garbage = self.get_input("Enter garbage expense: ")
        self.sewer = self.get_input("Enter sewer expense: ")
        self.hoa_bureauocrats = self.get_input("Enter Nosy Neighbor expense: ")
        self.lawn_ground_maintenance = self.get_input("Enter lawn/ground care expense: ")


    def get_input(self, prompt, multiplier=None):
        # Helper function to get input with validation
        while True:
            try:
                value = float(input(prompt))
                if multiplier is not None:
                    value *= multiplier  # Apply the multiplier if provided
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def input_security_expenses(self):
        # the cost of not being a parasite
        self.property_manager = self.get_input("Enter property manager expense (10%\n of rent recommended): ", multiplier=0.1)
        self.repair_fund = self.get_input("Enter repair fund expense ($50 - $100 a month per unit): ")
        self.vacancy = self.get_input("Enter vacancy expense (5%\n of rental income recommended): ", multiplier=0.05)
        self.capex = self.get_input("Enter capital expenditures expense (recommend $100 a month per unit): ")

    def calculate_total_expenses_group1(self):
    # Calculate total expenses for the first group
        total_expenses_group1 = (
        self.mortgage +
        self.taxes +
        self.insurance +
        self.electric +
        self.water +
        self.sewer +
        self.gas +
        self.garbage +
        self.hoa_bureauocrats +
        self.lawn_ground_maintenance
        )
        return total_expenses_group1
    
    def calculate_total_security_expenses(self):
    # total cost of not being a landleech
        total_security_expenses = (
        self.property_manager +
        self.repair_fund +
        self.vacancy +
        self.capex
        )
        return total_security_expenses

    def calculate_total_expenses(self):
        # Calculate total expenses by adding all expenses
        total_expenses = (
            self.calculate_total_expenses_group1() +
            self.calculate_total_security_expenses()
        )
        return total_expenses
    # box 3
    def calculate_cash_flow(self):
        #cash flow = total income - total expenses
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        cash_flow = total_income - total_expenses
        return cash_flow
    # box 4
    def input_investment_details(self):
        # Add up all the upfront costs
        self.down_payment = self.get_input("Enter down payment or purchase price: ")
        self.closing_costs = self.get_input("Enter closing costs: ")
        self.rehab_budget = self.get_input("Enter rehab budget: ")
        self.appraisal = self.get_input("Enter appraisal cost: ")
        self.inspection = self.get_input("Enter inspection cost: ")

    def calculate_total_investment(self):
        # calculate your total "investment"
        total_investment = (
            self.down_payment +
            self.closing_costs +
            self.rehab_budget +
            self.appraisal +
            self.inspection
        )
        return total_investment
    
    def calculate_roi(self):
    # Calculate Return on Investment (ROI)
        cash_flow = self.calculate_cash_flow()
        total_investment = self.calculate_total_investment()

        if total_investment == 0:
            return "Cannot calculate ROI with zero total investment."

        roi = (cash_flow / total_investment) * 100
        return roi

    def print_investment_summary(self):
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        total_investment = self.calculate_total_investment()
        roi = self.calculate_roi()

        print(f"\nTotal Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"ROI: {roi:.2f}%")

        if roi > 8:
            print("This is a high return investment.")
        elif 3 <= roi <= 8:
            print("This is an average return investment.")
        else:
            print("This is a money pit.")

    # RUN THEM NUMBERS!!!
calculator = HomeScalpingCalculator(
    monthly_rent_studio=0, monthly_rent_1br=0, monthly_rent_2br=0, monthly_rent_3br=0,
    laundry=0, storage=0, covered_parking=0,
    num_studio=0, num_1br=0, num_2br=0, num_3br=0, num_storage=0, num_covered_parking=0,
    mortgage=0, taxes=0, insurance=0, electric=0, water=0, sewer=0, gas=0, garbage=0,
    robber_barons=0, grounds_crew=0, property_manager=0, repair_fund=0, vacancy=0, capex=0, purchase_price=0
)

# Input details
calculator.income_details()
calculator.input_expenses()
calculator.input_security_expenses()
calculator.input_investment_details()

# Calculate and print the summary
calculator.print_investment_summary()
