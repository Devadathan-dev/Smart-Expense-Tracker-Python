import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict
import os
import subprocess

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


categories = ['Food', 'Auto', 'Gold', 'Bills', 'Travel', 'Shopping']

def load_data():
    try:
        with open('expenses.csv', 'r' , encoding='utf-8') as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        print("file not found")
        return []

def add_expense():
    print("\n=== Add Expense ===")
    
    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    BUDGET_LIMIT = 50000  
    data = load_data()
    total_spent = sum(float(row[2]) for row in data if len(row) >= 3) if data else 0

    if total_spent + amount > BUDGET_LIMIT:
        print(f"⚠️ Warning: ₹{total_spent + amount - BUDGET_LIMIT:.0f} over budget!")
        if input("Continue anyway? (y/n): ").lower() != 'y':
            return


    print("Categories:", ", ".join(categories))
    category = input("Category: ").title()

    if category not in categories:
        print("❌ Invalid category.")
        return
    
    note = input("Note: ")
    
    with open('expenses.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime('%Y-%m-%d'), category, amount, note])
    
    print("✅ Expense added.")

def show_report():
    data = load_data()
    if not data: 
        print("No expenses yet")
        return
    
    df = [[row[0], row[1], float(row[2])] for row in data if len(row)>=3]

    total = sum(row[2] for row in df)
    
    print(f"\n💰 Total: ₹{total:.2f}")
    
    
    cat_total = defaultdict(float)
    for date, cat, amt in df:
        cat_total[cat.title()] += amt
    
    print("\nBy Category:")
    for cat, amt in cat_total.items():
        print(f"  {cat}: ₹{amt:.2f}")

def show_chart():
    data = load_data()
    if not data:
        print("No expenses to show.")
        return
    
    cats = defaultdict(float)
    for row in data:
        if len(row) >= 3:
            cats[row[1].title()] += float(row[2])


    plt.bar(cats.keys(), cats.values())
    plt.title("Expense Breakdown")
    plt.ylabel("₹ Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('expenses.png', dpi=300, bbox_inches='tight')
    print("📊 Chart saved as expenses.png")
    plt.show()


while True:
    print("\n=== Smart Expense Tracker ===")
    print("1. Add Expense  2. Report  3. Chart  4. Exit")
    choice = input("Choose: ")
    
    if choice == '1': add_expense()
    elif choice == '2': show_report()
    elif choice == '3': show_chart()
    elif choice == '4': break
    else :
        print("Invalid Choice")
