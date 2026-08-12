from expense import Expense,RecurringExpense
import datetime
import json
def save_expenses(expenses, filename="expenses.json"):
    expenses = [exp.to_dict() for exp in expenses]

    with open(filename, "w") as f:
        json.dump(expenses,f)

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_data = json.load(f)

        expenses = []
        for item in file_data:
            parsed_date = datetime.datetime.strptime(item["date"], "%Y-%m-%d").date()
            item["date"] = parsed_date
            if item.get("type") == "recurring expense":
                obj = RecurringExpense.from_dict(item)
            else:
                obj = Expense.from_dict(item)

            expenses.append(obj)

            return expenses

    except (FileNotFoundError,json.JSONDecodeError):
            print("no file found or is empty")
            return []
