import datetime
from expense_manager import Manage_Expense
from expense import Expense

if __name__ == '__main__':
    # operation = {
    #     'Add Expense':'Add',
    #     'Delete Expense':'Delete',
    #     'List Expenses':'List'
    # }
    a = input(f'Choose from below operations:\nAdd\nList\nDelete\n')

    if a.lower() == 'add':
        category = input(f'Choose from below category of expense\n{','.join(Expense.category)}: ')
        if category not in Expense.category:
            raise Exception("Invalid Category Selected")
        try:
            amount = int(input('Enter amount of expense: '))
            if  amount < 0:
                raise Exception("Invalid Amount Selected")
        except ValueError:
            raise ValueError("Invalid Amount Selected")
        except TypeError:
            raise TypeError("Invalid Amount Selected")
        description = input('Choose description of expense: ')
        exp1 = Manage_Expense()
        id = exp1.computeId()

        expense = Expense(
            id= id,
            category = category,
            amount = amount,
            date = datetime.date.today().isoformat(),
            description = description
        )
        exp1.addExpense(expense)
    elif a.lower() == 'list':

        Manage_Expense().listExpense()
    elif a.lower() == 'delete':
        id = input('Choose expense id to delete:')
        expense = Manage_Expense()
        expense.deleteExpense(id)
    else:
        raise "Invalid Operation Selected"



