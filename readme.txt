Budget and expense tracking app:

An interface that shows your current total bank balance that was inserted when is opened for the first time.
You would be able to add multiple bank accounts with its bank balance. If more added, the interface will show both banks' balance.

At the start, we have to determine budgets that the user can define themselves. e.g. I want a budget of 100k for monthly investing, a budget of 200k for expenditures.
Then we also want to add expenses and profits that influence the bank balance. These expenses then are also categorized based on the budgets we have given, if no category was given, make it a default expense.
When we do however add an expense/profit with a budget, make the interface show a warning if we are close to reaching the max of the budget.


Objects:
    - Interface as a menu
        +Read bank balance and print
        +Deduct this expense from the total balance
        +If expense details includes budget category, deduct from set budget amount
        +If budget is 20% from 0, warn the user that budget almost is capped.

    - Bank accounts
        +Insert bank accounts + balance

    - budgets
        +Insert budget type and its amount

    - Expense/profit
        +Insert new expense/income with details

Methods:
    - Insert bank accounts + balance
    - Insert budget type and its amount
    - Insert new expense/income with details
    - Deduct this expense from the total balance
    - If expense details includes budget category, deduct from set budget amount
    - If budget is 20% from 0, warn the user that budget almost is capped.

Directory structure:
    \main
        budget_menu.py
        \budgeting
            budget_bank_setup.py
            budget_incoming_outgoing.py

