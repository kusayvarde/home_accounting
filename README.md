# 🏠 Home Shared Accounting App

A simple and intuitive Streamlit application for managing shared expenses among housemates. Track who paid for what, who used what, and automatically calculate who owes whom.

## 📋 Features

- **Easy Expense Tracking**: Add expenses with item name, cost, who paid, and who used it
- **Automatic Balance Calculation**: Instantly see who should pay and who should receive money
- **Customizable Participants**: Add or remove people from your household
- **Clean Interface**: Simple, user-friendly Streamlit interface
- **Real-time Updates**: See balances update as you add expenses

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip or uv package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd home_accounting
```

2. Install dependencies:

Using pip:
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv pip install -e .
```

### Running the Application

Start the Streamlit app:
```bash
streamlit run main.py
```

The app will open in your default web browser at `http://localhost:8501`

## 💡 How to Use

1. **Set Up Participants**: 
   - In the sidebar, enter the names of people in your household separated by commas
   - Default: A, B, C, D, E, F, G

2. **Add an Expense**:
   - Enter the item name (e.g., "Groceries", "Tomatoes", "Electricity bill")
   - Enter the total cost in Turkish Lira (₺)
   - Select who paid for the item
   - Select who used/benefited from the item (can be multiple people)
   - Click "Add Expense"

3. **View Balances**:
   - The app automatically calculates and displays:
     - Who should receive money (positive balance)
     - Who should pay money (negative balance)
     - Who is settled (zero balance)

4. **Clear Data**:
   - Click "🧹 Clear All Expenses" to start fresh

## 📊 Example

If Alice buys groceries for ₺100 that are used by Alice, Bob, and Charlie:
- Alice initially pays ₺100
- Each person owes ₺33.33 (100/3)
- Alice's balance: +₺66.67 (she should receive)
- Bob's balance: -₺33.33 (he should pay)
- Charlie's balance: -₺33.33 (he should pay)

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **Python 3.12+**: Programming language

## 📝 Project Structure

```
home_accounting/
├── main.py           # Main application file
├── pyproject.toml    # Project dependencies and metadata
└── README.md         # This file
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

Built for shared household expense tracking.

---

Made with ❤️ using Streamlit