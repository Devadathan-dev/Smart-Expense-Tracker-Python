import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

expenses = []
categories = ['Food', 'Auto', 'Gold', 'Bills', 'Travel', 'Shopping']

def load_data():
    try:
        with open('expenses.csv', 'r') as f:
            return list(csv.reader(f))
    except:
        return []

def add_expense():
    print("\n=== Add Expense ===")
    amount = float(input("Amount (₹): "))
    BUDGET_LIMIT = 50000  # Your monthly budget
    total_spent = sum(float(row[2]) for row in load_data()) if load_data() else 0
    if total_spent + amount > BUDGET_LIMIT:
        print(f"⚠️ Warning: ₹{total_spent+amount-BUDGET_LIMIT:.0f} over budget!")

    category = input(f"Category ({'/'.join(categories)}): ")
    note = input("Note: ")
    
    with open('expenses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime('%Y-%m-%d'), category, amount, note])

def show_report():
    data = load_data()
    if not data: 
        print("No expenses yet")
        return
    
    df = [[row[0], row[1], float(row[2])] for row in data]
    total = sum(row[2] for row in df)
    
    print(f"\n💰 Total: ₹{total:.2f}")
    
    # Category breakdown
    cat_total = defaultdict(float)
    for date, cat, amt in df:
        cat_total[cat] += amt
    
    print("\nBy Category:")
    for cat, amt in cat_total.items():
        print(f"  {cat}: ₹{amt:.2f}")

def show_chart():
    data = load_data()
    if not data: return
    
    cats = defaultdict(float)
    for row in data:
        cats[row[1]] += float(row[2])
    plt.savefig('expense_chart.png', dpi=300, bbox_inches='tight')
    print("📊 Chart saved: expense_chart.png")

    
    plt.bar(cats.keys(), cats.values())
    plt.title("Expense Breakdown")
    plt.ylabel("₹ Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.savefig('expenses.png')
    print("📊 Chart saved as expenses.png")

while True:
    print("\n=== Smart Expense Tracker ===")
    print("1. Add Expense  2. Report  3. Chart  4. Exit")
    choice = input("Choose: ")
    
    if choice == '1': add_expense()
    elif choice == '2': show_report()
    elif choice == '3': show_chart()
    elif choice == '4': break
