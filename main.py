from manage_expense import Manage_Expense
from expense import Expense

if __name__ == '__main__':
    operation = {
        'Add Expense',
        'Delete Expense',
        'List Expenses',
    }
    a = input(f'Choose of operation: {operation}')

    if a == 'Add Expense':
        category = input(f'Choose category of expense i.e. {Expense.category}: ')
        amount = input('Choose amount of expense: ')
        description = input('Choose description of expense: ')
        exp1 = Manage_Expense(
            category = category,
            amount = amount,
            description = description
        )
        exp1.addExpense()



