import datetime
from budget_movement.budget_incoming_outgoing import Expense

# Each bank will have a unique ID
bank_id = 0

class BankDetails:
    def __init__(self, name, balance):
        """Adding the bank details and its current balance"""
        self.bank_name = name
        self.balance = balance
        self.last_update = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-$Y")
        global bank_id
        bank_id += 1
        self.bank_id = bank_id

    def adjust_balance(self, balance):
        """It is recommended to only use this when the balance was wrongly
        inserted from the start. Balance should mainly be adjusted by
        expenses or incomes, not by manual adjustments."""
        self.balance = balance
        self.last_update = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-$Y")

    def add_movement(self, amount):
        self.balance += amount
        self.last_update = datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-$Y")

    def secondary_details(self, location, contact_person):
        """If we want to be more specific regarding the bank, use this."""
        self.location = location
        self.person = contact_person

#Each budget will have a unique ID
budget_id = 0

class BudgetDetails:
    def __init__(self, name, amount):
        """Add a new budget by specificying a new and amount"""
        self.budget_name = name
        self.budget_amount = amount
        global budget_id
        budget_id += 1
        self.id = budget_id
    
    def rename_budget(self, name):
        """Rename the budget for any reason"""
        self.budget_name = name
    
    def adjust_amount(self, amount):
        """adjust_amount only is for when the budget was wrongly inserted from
        the start. For adjustments caused by income/expenses, do not use this method"""
        self.budget_amount = amount
    
    def add_movement(self, amount):
        """Based on expenses, will always deduct from budget."""
        self.budget_amount += amount

class BudgetApp:
    def __init__(self):
        """For each bank, will append to the list, same goes for budgets."""
        self.banks = []
        self.budgets = []
        self.expenses = []
    
    def add_bank(self, name, balance):
        self.banks.append(BankDetails(name, balance))
    
    def remove_bank(self, id):
        del self.banks[1 - id]
    
    def add_budget(self, name, amount):
        self.budgets.append(BudgetDetails(name, amount))

    def remove_budget(self, id):
        del self.budgets[1 - id]

    def add_expense(self, bank_id, amount, info, budget=None):
        for bank in self.banks:
            if bank_id == bank.bank_id:
                self.expenses.append(Expense(bank_id, amount, info, budget=None))
                bank.add_movement(amount)

                if budget and self.budgets:
                    self.add_budget_movement(amount, budget)
                return True
        return False

    def revert_expense(self, id, amount, budget=None):
        for bank in self.banks:
            if bank.bank_id == id:
                bank.add_movement(+amount)

                if budget:
                    for b in self.budgets:
                        if budget == b.budget_name:
                            b.add_movement(+amount)
        
    def add_budget_movement(self, amount, budget):
        for b in self.budgets:
            if budget == b.budget_name:
                b.add_movement(amount)
                return True
        return False
    
    
    
    


    




    

