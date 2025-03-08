import pandas as pd
import csv
from datetime import datetime
from data_entry import get_category, get_amount, get_date, get_description
import matplotlib.pyplot as plt
class CSV:
    date_format = "%d-%m-%Y"
    CSV_File = "finance_data.csv"
    columns = ["date","amount","category","description"]
    @classmethod #access to class only not to an instance
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.CSV_File, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_File,"a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.columns)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_File)
        df["date"] = pd.to_datetime(df["date"], format=CSV.date_format)
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(
                f"Transaction from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.date_format)}
                    )
                )

            total_income = filtered_df[filtered_df['category'] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df['category'] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")


            return filtered_df





def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date:",allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

def plot_transaction(df):
    df.set_index('date',inplace=True)
    income_df = (
        df[df['category'] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df['category'] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df['amount'], label='Income', color='g')
    plt.plot(expense_df.index, expense_df['amount'], label='Expense', color='r')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses over time")
    plt.legend()
    plt.grid(True)
    plt.show()




def main():
    while True:
        print("\n1. Add a new transaction:")
        print("2. View transaction and summary within a date range:")
        print("3. Exit:")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy):")
            end_date = get_date("Enter the end date (dd-mm-yyyy):")
            df = CSV.get_transaction(start_date,end_date)
            if input("Do you want to see a plot? (y/n)").lower() ==  'y':
                plot_transaction(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, Enter 1,2 or 3.")

if __name__ == "__main__":
    main()

# flet app
# import flet as ft
# import pandas as pd
# import csv
# import matplotlib.pyplot as plt
# from datetime import datetime
#
# # Constants
# CSV_FILE = "finance_data.csv"
# COLUMNS = ["date", "amount", "category", "description"]
# DATE_FORMAT = "%d-%m-%Y"
#
#
# # Initialize CSV file
# def initialize_csv():
#     try:
#         pd.read_csv(CSV_FILE)
#     except FileNotFoundError:
#         df = pd.DataFrame(columns=COLUMNS)
#         df.to_csv(CSV_FILE, index=False)
#
#
# initialize_csv()
#
#
# # Function to add transaction
# def add_transaction(date, amount, category, description):
#     new_entry = {"date": date, "amount": amount, "category": category, "description": description}
#     with open(CSV_FILE, "a", newline="") as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
#         writer.writerow(new_entry)
#
#
# # Function to read transactions
# def get_transactions():
#     df = pd.read_csv(CSV_FILE)
#     if df.empty:
#         return []
#     df = df.tail(10)  # Show only last 10 transactions for UI simplicity
#     return df.to_dict(orient="records")
#
#
# # Generate and save plot
# def generate_plot():
#     df = pd.read_csv(CSV_FILE)
#     df["date"] = pd.to_datetime(df["date"], format=DATE_FORMAT)
#
#     if df.empty:
#         return None
#
#     df.set_index("date", inplace=True)
#
#     # Aggregate Income & Expense
#     income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
#     expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)
#
#     plt.figure(figsize=(10, 5))
#     plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
#     plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
#     plt.xlabel("Date")
#     plt.ylabel("Amount")
#     plt.title("Income and Expenses Over Time")
#     plt.legend()
#     plt.grid(True)
#
#     chart_path = "chart.png"
#     plt.savefig(chart_path)
#     plt.close()
#     return chart_path
#
#
# # Flet App
# def main(page: ft.Page):
#     page.title = "Finance Tracker"
#     page.window_width = 700
#     page.window_height = 600
#     page.scroll = "adaptive"  # Allow scrolling
#
#     # UI Elements
#     date_field = ft.TextField(label="Date (dd-mm-yyyy)", value=datetime.today().strftime(DATE_FORMAT))
#     amount_field = ft.TextField(label="Amount", keyboard_type=ft.KeyboardType.NUMBER)
#     category_field = ft.Dropdown(
#         label="Category",
#         options=[ft.dropdown.Option("Income"), ft.dropdown.Option("Expense")]
#     )
#     description_field = ft.TextField(label="Description")
#
#     transaction_list = ft.Column(scroll="always")
#     chart_image = ft.Image(src="", width=600, height=350, visible=False, fit=ft.ImageFit.CONTAIN)
#
#     # Load transactions
#     def load_transactions():
#         transaction_list.controls.clear()
#         transactions = get_transactions()
#         if transactions:
#             for txn in transactions:
#                 transaction_list.controls.append(
#                     ft.Text(f"{txn['date']} - {txn['amount']} - {txn['category']} - {txn['description']}")
#                 )
#         else:
#             transaction_list.controls.append(ft.Text("No transactions found."))
#         page.update()
#
#     # Add transaction
#     def on_add_click(e):
#         if not amount_field.value or not category_field.value or not description_field.value:
#             page.snack_bar = ft.SnackBar(ft.Text("Please fill all fields!"), bgcolor="red")
#             page.snack_bar.open = True
#             page.update()
#             return
#
#         add_transaction(date_field.value, float(amount_field.value), category_field.value, description_field.value)
#         load_transactions()
#         page.scroll_to("end")  # Scroll to bottom
#         page.snack_bar = ft.SnackBar(ft.Text("Transaction added successfully!"), bgcolor="green")
#         page.snack_bar.open = True
#         page.update()
#
#     # Update chart
#     def update_chart(e):
#         chart_path = generate_plot()
#         if chart_path:
#             chart_image.src = chart_path
#             chart_image.visible = True
#         else:
#             chart_image.visible = False
#         page.update()
#
#     # Buttons
#     add_button = ft.ElevatedButton("Add Transaction", on_click=on_add_click)
#     show_chart_button = ft.ElevatedButton("Show Chart", on_click=update_chart)
#
#     # Layout
#     page.add(
#         ft.Column(
#             [
#                 ft.Text("Finance Tracker", size=24, weight="bold"),
#                 date_field,
#                 amount_field,
#                 category_field,
#                 description_field,
#                 add_button,
#                 ft.Divider(),
#                 ft.Text("Recent Transactions:", size=18, weight="bold"),
#                 ft.Container(transaction_list, height=200, border=ft.border.all(1), padding=10),
#                 ft.Divider(),
#                 show_chart_button,
#                 ft.Container(chart_image, height=420, padding=10, border=ft.border.all(1)),
#             ],
#             spacing=10,
#         )
#     )
#
#     load_transactions()
#
#
# ft.app(target=main)

