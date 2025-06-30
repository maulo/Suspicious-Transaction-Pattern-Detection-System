# Suspicious-Transaction-Pattern-Detection-System

This project simulates a real-world AML/KYC analyst workflow to detect and flag suspicious banking transactions using rule-based logic. Built with Python and Excel, it helps identify potential red flags such as large transactions, abnormal frequency, and shared device usage — similar to patterns flagged in actual financial monitoring systems.

Project Files

**`generate_transactions.py**→ Creates 5,000 fake banking transactions using Faker and exports to Excel
**detect_suspicious.py** → Applies 3 AML rules and flags suspicious transactions
**synthetic_transactions.xlsx** → Raw transaction data (auto-generated)
**suspicious_transactions_report.xlsx** → Final filtered report with flagged transactions
*Excel Dashboard* → Built using filters, slicers, and conditional formatting (no PivotTables)



# Detection Logic
                                                                       |
**Rule 1** Transactions over ₹10,00,000                                            
**Rule 2** High-value transactions by the same account on the same day
**Rule 3** Same device ID used by 5 or more different accounts                     



# Tools Used

**Python** (v3.13)  
**Libraries**: `pandas`, `openpyxl`, `faker`  
**Excel** for reporting, filtering, and dashboard creation



# Output Sample (Excel Report)

The `suspicious_transactions_report.xlsx` file includes:
`transaction_id`, `account_id`, `txn_amount`, `txn_time`, `location`, `device_id`
**Flags**: `high_value_flag`, `freq_flag`, `device_flag`, `suspicious`



# How to Run Locally

1. Install Python 3.13+
2. Install required libraries:

   pip install pandas openpyxl faker

3. Run the scripts:
python generate_transactions.py
python detect_suspicious.py
4. Open the Excel file suspicious_transactions_report.xlsx for results.

