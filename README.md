# 🏦 ATM Machine Simulator (Python OOP)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An interactive **ATM Machine Simulator** built in Python using **Object-Oriented Programming (OOP)** principles. Designed with a clean CLI interface and security features to simulate real-world ATM operations.  

🎥 **[Watch Demo Video](https://your-demo-link-here)**

---

## ✨ Features
✅ User account creation with:
- Name, account number, PIN, and initial deposit  
- Security question for account recovery  

✅ Core operations:  
- 💵 Deposit funds  
- 💸 Withdraw funds  
- 🔄 Transfer funds between accounts  
- 🧾 View transaction history  
- 🔐 Change PIN with validation  
- 🔒 Account lockout after 3 failed PIN attempts  

✅ User-friendly CLI:
- 📜 Colored text (green for success, red for errors)  
- 🖥️ ASCII art welcome screen  
- 📊 PrettyTable menus for options  

---

## 🖥️ Tech Stack
- 🐍 **Python 3.x**  
- 🎨 ANSI colors for a beautiful terminal UI  
- 📦 [PrettyTable](https://pypi.org/project/prettytable/) for menu display  

---

## 📂 Project Structure

```bas
ATM-Machine-Simulator/
│
├── main.py                         # Entry point of the simulator
│
├── atm/                            # Core logic package
│   ├── account.py                  # Account class (balance, name, PIN, etc.)
│   ├── transaction.py              # Deposit, Withdraw, Transfer logic
│   ├── atm_machine.py              # ATM Machine class: manages user interactions & reports
│   └── bank.py                     # (Optional) Bank class for managing multiple accounts
├── tests/                          # Automated tests
│   ├── test_account.py             # Tests for account.py
│   ├── test_transaction.py         # Tests for transaction.py
│   ├── test_atm_machine.py         # Tests for atm_machine.py
│   └── __init__.py                 # Makes this a Python package
│
├── README.md                       # Project overview, installation & usage instructions
├── requirements.txt                # List of dependencies (e.g., pytest)
└── LICENSE                         # Your chosen license (e.g., MIT)
```
---

## ▶️ How to Run
1️⃣ Clone the repository:
```bash
git clone https://github.com/thesibaram/ATM-Machine-Simulator.git
cd ATM-Machine-Simulator
```
## 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
## 3️⃣ Run the simulator:
```bash
python main.py
```

## 🙌 Contribution
Want to contribute? Fork this repo and submit a pull request.

## 📜 License
This project is licensed under the MIT License.



