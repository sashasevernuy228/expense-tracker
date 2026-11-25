class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})

    def total(self):
        return sum(e["amount"] for e in self.expenses)

    def total_by_category(self, category):
        return sum(e["amount"] for e in self.expenses if e["category"] == category)

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)