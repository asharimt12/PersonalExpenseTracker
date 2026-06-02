
from tabulate import tabulate
from storage import Storage


class Manage_Expense:
    def computeId(self):
        expenses = Storage.load()
        if expenses==[]:
            return 1
        else:
            return expenses[-1]['Id']+1

    def addExpense(self, expense):

        expense_dict = {
            'Id': expense.id,
            'Category': expense.category,
            'Amount': expense.amount,
            'Description': expense.description,
            'Date': expense.date
        }

        expenses = Storage.load()
        expenses.append(expense_dict)
        Storage.save(expenses)


    def deleteExpense(self, id):
        expenses = Storage.load()
        for expense in expenses:
            if expense['Id']==id:
                expenses.remove(expense)
        Storage.save(expenses)

    def listExpense(self):
        headers = ['Id', 'Category', 'Amount', 'Description', 'Date']
        expenses = Storage.load()
        rows = [[expense['Id'], expense['Category'], expense['Amount'], expense['Description'], expense['Date']]
                for expense in expenses]
        table = tabulate(rows, headers=headers, tablefmt="fancy_grid")
        print('\nExpense List\n' + '\n' + table)
