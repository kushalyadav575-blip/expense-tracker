def total_by_category(expenses):
    category_expenses={}
    for item in expenses:
        category_expenses[item.category] = category_expenses.get(item.category,0) + item.amount
    return category_expenses

def total_spent(expenses):
    return sum(item.amount for item in expenses)

def monthly_total(expenses, year, month):
    return sum(item.amount for item in expenses if year==item.expense_date.year and month==item.expense_date.month)

def top_category(expenses):
    category_expenses=total_by_category(expenses)
    return max(category_expenses,key=category_expenses.get)

def filter_by_category(expenses, category):
    return [item for item in expenses if item.category==category]