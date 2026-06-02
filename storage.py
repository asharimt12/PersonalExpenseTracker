import json


class Storage:
    @staticmethod
    def save(expenses):
        try:
            with open('./data/expenses.json','w') as expense_file:
                json.dump(expenses, expense_file)
        except FileNotFoundError as e:
            raise FileNotFoundError(
                '/data directory does not exist'
            ) from e

    @staticmethod
    def load():
        try:
            with open('./data/expenses.json', 'r') as expense_file:
                return json.load(expense_file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []