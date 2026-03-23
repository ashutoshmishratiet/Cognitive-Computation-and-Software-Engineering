"""
Create a sample normalized technical dataset for end-to-end testing
"""

import pandas as pd
import numpy as np
import os

# Create sample data with normalized indices
np.random.seed(42)
n_students = 50

data = {
    'Student_ID': [f'STU{i:03d}' for i in range(1, n_students + 1)],
    'CUI': np.random.uniform(0.65, 0.98, n_students),
    'CDI': np.random.uniform(0.60, 0.95, n_students),
    'CCI': np.random.uniform(0.68, 0.97, n_students),
}

df = pd.DataFrame(data)

# Round to 3 decimal places
for col in ['CUI', 'CDI', 'CCI']:
    df[col] = df[col].round(3)

# Save to Excel
output_path = r"c:\Users\Anshika Rana\OneDrive\Desktop\cogn\sample_normalized_dataset.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Sample normalized dataset created: {output_path}")
print(f"\nDataset Info:")
print(f"  - Records: {len(df)}")
print(f"  - Columns: {list(df.columns)}")
print(f"\nFirst 10 rows:")
print(df.head(10))
print(f"\nSummary Statistics:")
print(df[['CUI', 'CDI', 'CCI']].describe())
