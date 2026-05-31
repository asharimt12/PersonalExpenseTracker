import datetime

from expense import Expense
from storage import Storage


class Manage_Expense:
    def __init__(self, category, amount, description):
        self.id = self.computeId()
        self.category = category
        self.amount = amount
        self.description = description

    def computeId(self):
        return 1

    def addExpense(self):
        expense = Expense(
            id = self.id,
            category = self.category,
            amount = self.amount,
            description = self.description,
            date=datetime.date.today().isoformat()
        )
        Storage.save(expense)


    def deleteExpense(self):
        pass

    def listExpense(self):
        pass
