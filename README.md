# Finance-Tracker
# Finance Tracker Terminal App

## Overview
This is a simple finance tracking terminal-based application built in Python. It allows users to record income and expenses, view transaction history within a given date range, and visualize financial data using a line plot.

## Features
- **Add Transactions:** Record income and expenses with details such as date, amount, category, and description.
- **View Transactions:** Retrieve transactions within a specified date range and view a financial summary.
- **Visualize Data:** Generate a plot of income and expenses over time.
- **Persistent Storage:** Transactions are stored in a CSV file for future reference.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/finance-tracker.git
   cd finance-tracker
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the application using:
```sh
python main.py
```
You will be prompted with options to add transactions, view transactions, and exit the application.

### Adding a Transaction
1. Enter the date (or press enter for today's date).
2. Input the amount.
3. Select a category (`I` for Income, `E` for Expense).
4. Provide a description.

### Viewing Transactions
1. Enter a start date and an end date.
2. The application will display all transactions within the specified range along with a summary of total income, expenses, and net savings.
3. You will be given the option to generate a visualization of income and expenses over time.

## File Structure
```
finance-tracker/
│── main.py            # Main application script
│── data_entry.py      # Helper functions for user input
│── finance_data.csv   # CSV file storing transaction data
│── requirements.txt   # List of dependencies
│── README.md          # Project documentation
```

## Dependencies
- `pandas`
- `matplotlib`

Install them using:
```sh
pip install pandas matplotlib
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this project and submit pull requests with improvements.

## Author
Your Name - [GitHub Profile](https://github.com/yourusername)

