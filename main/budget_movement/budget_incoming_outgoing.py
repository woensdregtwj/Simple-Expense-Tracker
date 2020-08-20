import datetime

expense_id = 0

class Expense:
    def __init__(self, bank_id, amount, info, budget=None):
        self.bank_id = bank_id
        self.amount = amount
        self.info = info
        self.budget = budget
        self.date = datetime.datetime.now()
        global expense_id
        expense_id += 1
        self.expense_id = expense_id
