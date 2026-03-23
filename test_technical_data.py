import pandas as pd
import numpy as np
import os

# Create test technical dataset with normalized CUI, CDI, CCI (0-1 range)
np.random.seed(42)
n_students = 50

data = {
    'Student_ID': [f'STU{i:03d}' for i in range(1, n_students + 1)],
    'CUI': np.round(np.random.uniform(0.3, 0.95, n_students), 3),  # Understanding Index
    'CDI': np.round(np.random.uniform(0.4, 0.90, n_students), 3),  # Debugging Index
    'CCI': np.round(np.random.uniform(0.2, 0.85, n_students), 3),  # Completion Index
}

df = pd.DataFrame(data)

# Save as Excel file
output_path = os.path.join(os.path.dirname(__file__), 'sample_technical_dataset.xlsx')
df.to_excel(output_path, index=False, sheet_name='Technical Data')

print(f"✓ Test dataset created: {output_path}")
print(f"  Records: {len(df)}")
print(f"  Columns: {', '.join(df.columns)}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nColumn ranges:")
print(df[['CUI', 'CDI', 'CCI']].describe())
