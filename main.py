# How to get the Memory size of a DataFrame in Pandas

import pandas as pd

df = pd.DataFrame({
    'Name': [
        'Alice',
        'Bobby',
        'Carl'
    ],
    'Date': [
        '2023-07-12',
        '2023-08-23',
        '2023-08-21'
    ]
})

# Index    128
# Name      24
# Date      24
# dtype: int64
print(df.memory_usage())

print('-' * 50)

print(df.memory_usage(index=True).sum())  # 👉️ 176