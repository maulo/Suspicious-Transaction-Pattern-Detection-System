import pandas as pd
import numpy as np
from faker import Faker

faker = Faker()
data = []

for _ in range(5000):
    data.append({
        "transaction_id": faker.uuid4(),
        "account_id": faker.bothify(text='A###'),
        "txn_amount": np.random.randint(100, 2000000),
        "txn_type": np.random.choice(['CREDIT', 'DEBIT']),
        "txn_time": faker.date_time_this_year(),
        "location": faker.city(),
        "device_id": faker.bothify(text='D###')
    })

df = pd.DataFrame(data)
df.to_excel('synthetic_transactions.xlsx', index=False)
print("✅ Excel file created: synthetic_transactions.xlsx")
