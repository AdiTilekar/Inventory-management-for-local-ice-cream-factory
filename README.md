# Shri Ganesh Kulfi - Inventory & Billing System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/static/v1?label=Made%20with&message=love&color=red" alt="Made with Love">
</p>

<p align="center">
A simple, command-line based inventory management and billing system designed for a kulfi shop. This project helps shopkeepers efficiently manage kulfi stock, generate instant bills, and maintain sales records.
</p>



---

## 📖 Table of Contents
- [✨ Features](#-features)
- [📋 Kulfi Menu](#-kulfi-menu)
- [🚀 Getting Started](#-getting-started)
- [💡 How to Use: A Sample Walkthrough](#-how-to-use-a-sample-walkthrough)
- [🗂️ Files Generated](#️-files-generated)
- [📂 Project Structure](#-project-structure)
- [🔮 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## ✨ Features
- **User-Friendly CLI:** A clean and simple command-line interface.
- **Dynamic Inventory:** Stock is automatically updated after each sale.
- **Persistent Storage:** Inventory state is saved in `rec.json` and all transactions are logged in `sales.csv`.
- **Real-time Billing:** Generates bills on the fly with accurate amount calculation.
- **Data Logging:** Records customer details and purchase history for every transaction.

---

## 📋 Kulfi Menu
| Product ID | Kulfi Name        | Price (₹) |
|------------|-------------------|-----------|
| `101`      | Mava Kulfi        | 10        |
| `102`      | Chocolate Kulfi   | 25        |
| `103`      | Jamun Kulfi       | 25        |
| `104`      | Gulkand Kulfi     | 25        |
| `105`      | Dryfruit Kulfi    | 25        |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation & Running the Program
1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/your-username/shri-ganesh-kulfi.git](https://github.com/your-username/shri-ganesh-kulfi.git)
    ```
2.  Navigate into the project directory:
    ```bash
    cd shri-ganesh-kulfi
    ```
3.  Run the main program file from your terminal:
    ```bash
    python kulfi_inventory.py
    ```
---

## 💡 How to Use: A Sample Walkthrough

The program will guide you through the entire process, from updating stock to making a sale. Below is a complete example of what you'll see in your terminal.

1.  **First, you'll be asked to update the initial inventory:**
    ```
    ========================================
        UPDATE INITIAL KULFI INVENTORY
    ========================================
    Enter stock for Mava Kulfi (101): 10
    Enter stock for Chocolate Kulfi (102): 5
    Enter stock for Jamun Kulfi (103): 7
    Enter stock for Gulkand Kulfi (104): 3
    Enter stock for Dryfruit Kulfi (105): 8
    ```
2.  **Next, enter the customer's details and the purchase information:**
    ```
    ========================================
            CUSTOMER & BILLING DETAILS
    ========================================
    Enter Customer Name: Rahul
    Enter Mail ID      : rahul@example.com
    Enter Number       : 9876543210

    Enter Product ID   : 102
    Enter Quantity     : 2
    ```
3.  **The system will then generate the bill and confirm the transaction:**
    ```
    ----------------------------------------
              ** Shri Ganesh Kulfi **
    ----------------------------------------
    Name     : Chocolate Kulfi
    Price    : 25
    Quantity : 2
    ----------------------------------------
    Billing Amount : 50
    ----------------------------------------

    ✅ Inventory in rec.json has been updated.
    ✅ Transaction logged successfully in sales.csv.
    ```
---

## 🗂️ Files Generated
-   `rec.json` → A JSON file that stores the latest stock count for all kulfi flavors.
-   `sales.csv` → A CSV file that logs every transaction with customer and purchase details.

---

## 📂 Project Structure
 ```
kulfi-inventory/
│

├── kulfi_inventory.py     # Main program script

├── rec.json               # Auto-generated inventory file

├── sales.csv              # Auto-generated sales log

└── README.md              # Project documentation
 ```

---

## 🔮 Roadmap
Future enhancements planned for the project:
- [ ] Develop a Graphical User Interface (GUI) using Tkinter or PyQT.
- [ ] Implement a feature to generate and print/save PDF bills.
- [ ] Add a login system for different staff members.
- [ ] Introduce functionality for discounts and promotional offers.
- [ ] Create a dashboard for sales reports and analytics.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request. You can also open an issue with the "enhancement" tag to suggest new features.

---

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
