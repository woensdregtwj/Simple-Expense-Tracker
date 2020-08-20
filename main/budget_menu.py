from budget_movement.budget_bank_details import BankDetails, BudgetDetails, BudgetApp
from budget_movement.budget_incoming_outgoing import Expense

import time
import sys

class BudgetInterface:
    def __init__(self):
        self.budgeting = BudgetApp()
        self.menu_options()

    def menu_options(self):
        """Based on user input value, we activate one of the methods.
        All methods are connected to a key within the dictionary."""
        self.menu = {
            "1": self.show_bank,
            "2": self.add_bank,
            "3": self.show_budget,
            "4": self.add_budget,
            "5": self.current_expenses,
            "6": self.add_expense,
            "7": self.revert_expense,
            "8": self.manual_bank_adjust,
            "9": self.manual_budget_adjust,
            "10": self.remove_bank,
            "11": self.remove_budget,
            "12": sys.exit,
        }
    
    def run(self):
        while True:
            time.sleep(2)
            print(
                """
                Budget Application
                Please type your action

                1. Show bank details and balance
                2. Add new bank details and balance

                3. Show active budgets
                4. Add new budget

                5. Show current expenses
                6. Add new expense
                7. Revert expense

                8. Adjust total bank balance
                9. Adjust total budget amount

                10. Remove bank
                11. Remove budget

                12. Quit
                """
            )
            action = input("Enter your action: ")

            choice = self.menu.get(action)
            if choice:
                choice()
            else:
                print(f"Not a valid option.")

    def show_bank(self):
        """Will neatly print out the bank id, bank name, balance and last update"""
        if not self.budgeting.banks:
            print("There currently are no bank accounts connected.")
            return
        for bank in self.budgeting.banks:
            print(f"""ID {bank.bank_id}: {bank.bank_name}\nCurrent balance: 
            {format(bank.balance, ",")}\nLast updated on {bank.last_update}\n\n""")
    
    def add_bank(self):
        """Through user input, we add a new bank with its details"""
        name = input("Enter name of bank: ")
        amount = input("Enter current balance: ")
        self.budgeting.add_bank(name, int(amount))
        print(f"{name} has been added!")
    
    def show_budget(self):
        """Will neatly print out all the budgets set up by the user"""
        if not self.budgeting.budgets:
            print("There currently are no budgets set up.")
            return
        for budget in self.budgeting.budgets:
            print(f"ID {budget.id}: {budget.budget_name}\n{format(budget.budget_amount, ',')}")
    
    def add_budget(self):
        """Adding a new classification for a budget that includes an amount.
        When we specify a budget with an expense, the expense will also
        deduct from the budget."""
        name = input("Enter a name for your budget: ")
        amount = input("Enter a budget amount: ")
        self.budgeting.add_budget(name, int(amount))
        print(f"{name} has been added!")
    
    def current_expenses(self):
        """Displays all expenses that were inserted"""
        if not self.budgeting.expenses:
            print("There currently are no expenses made.")
            return
        for expense in self.budgeting.expenses:
            print(f"From Bank Account No. {expense.bank_id}\n \
            Amount: {expense.amount}\n \
            Details: {expense.info}\n \
            Within budget: {expense.budget}\n \
            Date issued: {expense.date}")
    
    def add_expense(self):
        """Add an expense that will automatically deduct the amount from
        the current balance of the specific bank account. If a budget name
        is given, then it will also deduct the amount from the budget."""
        self.show_bank()

        bank_id = input("Enter Bank ID for expense: ")
        amount = input("Enter expense amount: ")
        info = input("Enter details regarding the expense: ")
        budget = input("Enter budget name of this expense. If none, press enter: ")
        self.budgeting.add_expense(int(bank_id), int(-amount), info, budget)
        print("Succesfully added!")

    def revert_expense(self):
        """We are adding the expense back to the bank balance and also to the budget.
        After re-adding, we delete the expense from the expense list"""
        if not self.budgeting.expenses:
            print("There currently are no expenses made.")
            return
        for expense in self.budgeting.expenses:
            print(f"Payment ID: {expense.expense_id}\n \
            From Bank Account No. {expense.bank_id}\n \
            Amount: {expense.amount}\n \
            Details: {expense.info}\n")

        expense_id = input("Enter the payment ID you wish to revert: ")

        delete_expense = None
        for index, expense in enumerate(self.budgeting.expenses):
            if expense.expense_id == int(expense_id):
                self.budgeting.revert_expense(expense.bank_id, expense.amount, expense.budget)
                delete_expense = index
                break
        
        if delete_expense:
            del self.budgeting.expenses[delete_expense]
    
    def manual_bank_adjust(self):
        """If we ever have to adjust the total bank balance manually, we use this"""
        self.show_bank()
        bank_id = input("Enter Bank ID")
        amount = input("Enter new bank balance amount: ")

        for bank in self.budgeting.banks:
            if bank.bank_id == int(bank_id):
                bank.adjust_balance(amount)
                return
        
        self.show_bank()

    def manual_budget_adjust(self):
        """If you want to increase/decrease the budget, we use this."""
        self.show_budget()

        budget_id = input("Enter ID of budget: ")
        amount = input("Enter new budget amount: ")

        for b in self.budgeting.budgets:
            if b.budget_id == int(budget_id):
                b.adjust_amount = int(amount)
                return

        self.show_budget()
    
    def remove_bank(self):
        """Removing bank based on bank ID"""
        self.show_bank()

        id = input("Enter the Bank ID for being removed: ")

        remove_bank = None
        for index, bank in enumerate(self.budgeting.banks):
            if bank.bank_id == int(id):
                remove_bank = index
                break
        self.budgeting.remove_bank(remove_bank)

        self.show_bank()
    
    def remove_budget(self):
        """Removing budget based on budget name"""
        self.show_budget()

        budget_id = input("Enter Budget name for removal: ")

        remove_budget = None
        for index, b in enumerate(self.budgeting.budgets):
            if b.budget_id == int(budget_id):
                remove_budget = index
                break
        
        self.budgeting.remove_budget(remove_budget)

        self.show_budget()

if __name__ == "__main__":
    BudgetInterface().run()

    
        

    



# TODO - Create a budget alerter for when we have 20% remaining


    