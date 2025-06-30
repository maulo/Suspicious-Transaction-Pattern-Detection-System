import pandas as pd

# Load the Excel file
df = pd.read_excel("synthetic_transactions.xlsx")

# Ensure datetime format
df['txn_time'] = pd.to_datetime(df['txn_time'])
df['txn_date'] = df['txn_time'].dt.date

# RULE 1: Transactions over ₹10,00,000
df['high_value_flag'] = df['txn_amount'] > 1000000

# RULE 2: Accounts with more than 3 high-value transactions in a day
high_txns = df[df['txn_amount'] > 1000000]
grouped = high_txns.groupby(['account_id', 'txn_date']).size().reset_index(name='high_txn_count')
suspicious_accounts = grouped[grouped['high_txn_count'] > 3]
df['freq_flag'] = df.apply(lambda row: 
    ((row['account_id'], row['txn_date']) in 
     list(zip(suspicious_accounts['account_id'], suspicious_accounts['txn_date']))), axis=1)

# RULE 3: Same device used by 5+ accounts
device_counts = df.groupby('device_id')['account_id'].nunique()
suspicious_devices = device_counts[device_counts >= 5].index
df['device_flag'] = df['device_id'].isin(suspicious_devices)

# Final suspicious flag
df['suspicious'] = df[['high_value_flag', 'freq_flag', 'device_flag']].any(axis=1)

# Export only suspicious transactions to Excel
df[df['suspicious']].to_excel("suspicious_transactions_report.xlsx", index=False)
print("✅ Report saved: suspicious_transactions_report.xlsx")
