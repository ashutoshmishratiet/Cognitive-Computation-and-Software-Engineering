"""
Create a sample normalized Excel file for testing the technical upload workflow.
"""

import pandas as pd
import numpy as np
import os

# Seed for reproducibility
np.random.seed(42)

# Generate sample normalized data
n_participants = 20

# Generate normalized indices in domain [-0.25, 1.0]
u_s_values = np.random.uniform(-0.25, 1.0, n_participants)
d_s_values = np.random.uniform(-0.25, 1.0, n_participants)
c_s_values = np.random.uniform(-0.25, 1.0, n_participants)

# Create DataFrame with other potential columns that may exist in real data
data = {
    'Participant_ID': [f'P{i+1:03d}' for i in range(n_participants)],
    'Group': np.random.choice(['Control', 'Experimental'], n_participants),
    'U_S': u_s_values,  # Normalized Understanding Score
    'D_S': d_s_values,  # Normalized Debugging Score
    'C_S': c_s_values,  # Normalized Completion Score
    'Session': np.random.choice([1, 2, 3], n_participants),
    'Duration_minutes': np.random.randint(30, 120, n_participants)
}

df = pd.DataFrame(data)

# Save to Excel
output_file = 'sample_normalized_data.xlsx'
df.to_excel(output_file, index=False, sheet_name='Data')

print(f"✓ Sample normalized data file created: {output_file}")
print(f"  Participants: {n_participants}")
print(f"  Columns: {', '.join(df.columns.tolist())}")
print(f"\nDataFrame preview:")
print(df.head(10))
print(f"\nU_S range: [{df['U_S'].min():.4f}, {df['U_S'].max():.4f}]")
print(f"D_S range: [{df['D_S'].min():.4f}, {df['D_S'].max():.4f}]")
print(f"C_S range: [{df['C_S'].min():.4f}, {df['C_S'].max():.4f}]")
