import json


class Storage:
    def save(expense):
        expense_dict = {
            'Id':expense.id,
            'Category':expense.category,
            'Amount':expense.amount,
            'Description':expense.description,
            'Date':expense.date
        }
        with open('./data/expenses.json','a') as expense_file:
            json.dump(expense_dict, expense_file)

    def load(self):
        with open('./data/expenses.json','r') as expense_file:
            expense_dict = json.load(expense_file)
            return expense_dict
