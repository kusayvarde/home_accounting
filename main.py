import streamlit as st
import pandas as pd

# =================== Kusay,Hasan,Mustafa,Amr,Muhammed,Amer Z,Amer ====================

st.set_page_config(page_title="Home Accounting", page_icon="💰", layout="centered")

st.title("🏠 Home Shared Accounting App")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Step 1: Define people in the house
st.sidebar.header("People in the house")
people_input = st.sidebar.text_area("Enter names separated by commas:", "A, B, C, D, E, F, G")
people = [p.strip() for p in people_input.split(",") if p.strip()]

# Step 2: Add a new expense
st.header("➕ Add Expense")
with st.form("add_expense_form"):
    item = st.text_input("Item name (e.g., tomatoes)")
    cost = st.number_input("Total cost (₺)", min_value=0.0, step=5.0)
    paid_by = st.selectbox("Who paid?", people)
    used_by = st.multiselect("Who used it?", people, default=people)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if not item or cost <= 0 or not used_by:
            st.warning("Please fill all fields correctly.")
        else:
            st.session_state.expenses.append({
                "item": item,
                "cost": cost,
                "paid_by": paid_by,
                "used_by": used_by
            })
            st.success(f"Added expense for '{item}' ({cost}₺)")

# Step 3: Display all expenses
if st.session_state.expenses:
    st.header("📜 Expense List")
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    # Step 4: Calculate balances
    balances = {person: 0 for person in people}
    for expense in st.session_state.expenses:
        cost = expense["cost"]
        paid_by = expense["paid_by"]
        users = expense["used_by"]
        share = cost / len(users)

        balances[paid_by] += cost
        for user in users:
            balances[user] -= share

    # Step 5: Display results
    st.header("💸 Balances")
    results = []
    for person, balance in balances.items():
        if balance > 0:
            results.append({"Person": person, "Balance": f"+{balance:.2f}₺", "Status": "Should receive"})
        elif balance < 0:
            results.append({"Person": person, "Balance": f"-{-balance:.2f}₺", "Status": "Should pay"})
        else:
            results.append({"Person": person, "Balance": "0₺", "Status": "Settled"})

    results_df = pd.DataFrame(results)
    st.table(results_df)

    # total for person
    

    # Option to clear data
    if st.button("🧹 Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()

else:
    st.info("No expenses yet. Add one above!")

