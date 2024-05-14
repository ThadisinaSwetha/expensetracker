import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        self.expenses = []

        self.expense_label = tk.Label(master, text="Enter Expense:")
        self.expense_label.grid(row=0, column=0)

        self.expense_entry = tk.Entry(master)
        self.expense_entry.grid(row=0, column=1)

        self.amount_label = tk.Label(master, text="Enter Amount:")
        self.amount_label.grid(row=1, column=0)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=1, column=1)

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.show_button = tk.Button(master, text="Show Expenses", command=self.show_expenses)
        self.show_button.grid(row=3, column=0, columnspan=2)

        self.clear_button = tk.Button(master, text="Clear Expenses", command=self.clear_expenses)
        self.clear_button.grid(row=4, column=0, columnspan=2)

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        if expense and amount:
            self.expenses.append((expense, amount))
            messagebox.showinfo("Expense Added", "Expense added successfully!")
            self.expense_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both expense and amount.")

    def show_expenses(self):
        if self.expenses:
            expenses_text = "Expenses:\n"
            for expense, amount in self.expenses:
                expenses_text += f"{expense}: {amount}\n"
            messagebox.showinfo("Expenses", expenses_text)
        else:
            messagebox.showinfo("Expenses", "No expenses recorded yet.")

    def clear_expenses(self):
        self.expenses = []
        messagebox.showinfo("Expenses Cleared", "All expenses cleared successfully!")

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()