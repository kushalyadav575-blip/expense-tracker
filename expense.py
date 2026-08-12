import datetime
class InvalidAmountError(Exception):
    pass

class InvalidCategoryError(Exception):
    pass

class Expense:

    def __init__(self, amount, category, description="", expense_date=None):
        if amount <= 0:
            raise InvalidAmountError("amount is not valid")
        self.amount=amount
        self.category=category
        self.description=description
        
        if expense_date==None:
            self.expense_date=datetime.date.today()
        else:
            self.expense_date=expense_date

    def __str__(self):
        return f"{self.expense_date} {self.category}: {self.amount} ({self.description})"

    def to_dict(self):
        return {"type": "expense", "amount": self.amount, "category": self.category, "description": self.description, "date": self.expense_date.isoformat() }

    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"], data["description"], data["date"])
    
class RecurringExpense(Expense):

    def __init__(self, amount, category, frequency, description="", expense_date=None):
        super().__init__(amount, category, description, expense_date)
        self.frequency=frequency

    def __str__(self):
        return f"{super().__str__()} [Recurring: {self.frequency}]"

    def to_dict(self):
        new_dict=super().to_dict()
        new_dict["type"] = "recurring expense"
        new_dict["frequency"]=self.frequency
        return new_dict

    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"], data["frequency"], data["description"], data["date"])
    