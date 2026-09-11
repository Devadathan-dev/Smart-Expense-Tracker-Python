# Smart Expense Tracker

A simple Python CLI app for tracking expenses, with budget alerts and a category breakdown chart.

## Features

- Add expenses by category (Food, Auto, Gold, Bills, Travel, Shopping)
- Warns you if an expense would put you over a monthly budget
- Shows a report with totals per category
- Generates a bar chart of spending by category

## Run it

```
pip install -r requirements.txt
python tracker.py
```

## Files

- `tracker.py` - the app
- `expenses.csv` - where your expenses get saved (created automatically)
- `expenses.png` - chart generated from the "Chart" option

## Example

```
=== Smart Expense Tracker ===
1. Add Expense  2. Report  3. Chart  4. Exit
Choose: 1

=== Add Expense ===
Amount (₹): 1250
Categories: Food, Auto, Gold, Bills, Travel, Shopping
Category: Food
Note: Grocery shopping
✅ Expense added.
```