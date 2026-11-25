from src.expenses import ExpenseTracker

def test_add_expense():
    t = ExpenseTracker()
    t.add_expense(100, "food")
    assert t.total() == 100

def test_total_by_category():
    t = ExpenseTracker()
    t.add_expense(100, "food")
    t.add_expense(50, "food")
    assert t.total_by_category("food") == 150

def test_delete_expense():
    t = ExpenseTracker()
    t.add_expense(100, "food")
    t.delete_expense(0)
    assert t.total() == 0