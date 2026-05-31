class Expense:
    category = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Bills",
        "Healthcare",
        "Education",
        "Other"
    ]
    def __init__(self, id, date, category, amount, description):

        self.id = id
        self.date = date
        if category not in self.category:
            raise Exception(f"Expense category {self.category} does not exist")
        self.category = category
        self.amount = amount
        self.description = description



