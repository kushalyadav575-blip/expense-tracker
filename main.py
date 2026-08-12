from storage import load_expenses,save_expenses
import expense
import reports
expenses=load_expenses()

while True:
    choice=input("enter the corresponding number for the option you want to choose\n1. Add expense\n2. Add recurring expense\n3. List all expenses\n4. Show total by category\n5. Show total spent\n6. Show top category\n7. Filter by category\n8. Save & quit\n")

    if choice=="1":
        try:
            amount=int(input("enter the amount of the expense: "))
            category=input("enter the category of the expense: ")
            description=input("enter the description of the expense: ")
            item_expense=expense.Expense(amount,category,description)
            expenses.append(item_expense)
            print("expense succesfully added")
        except expense.InvalidAmountError:
            print("invalid input")

    elif choice=="2":
        try:
            amount=int(input("enter the amount of the expense: "))
            category=input("enter the category of the expense: ")
            description=input("enter the description of the expense: ")
            frequency=input("enter the frequencyof the expense: ")
            item_expense=expense.RecurringExpense(amount,category,frequency,description)
            expenses.append(item_expense)
            print("recurring expense succesfully added")
        except expense.InvalidAmountError:
            print("invalid input")

    elif choice=="3":
        for item in expenses:
            print(item)

    elif choice=="4":
        category_total=reports.total_by_category(expenses)
        for x,y in category_total.items():
            print(f"{x}:{y}")

    elif choice=="5":
        print(reports.total_spent(expenses))

    elif choice=="6":
        print(reports.top_category(expenses))

    elif choice=="7":
        category=input("enter category: ")
        print(reports.filter_by_category(expenses,category))

    elif choice=="8":
        save_expenses(expenses)
        print("expenses saved and exiting")
        break