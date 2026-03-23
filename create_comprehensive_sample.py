"""
Create a comprehensive sample Excel file with both technical and non-technical normalized indices.
"""

import pandas as pd
import numpy as np
import os

# Seed for reproducibility
np.random.seed(42)

# Generate comprehensive sample data
n_participants = 20

# Generate normalized indices
u_s_values = np.random.uniform(-0.25, 1.0, n_participants)
d_s_values = np.random.uniform(-0.25, 1.0, n_participants)
c_s_values = np.random.uniform(-0.25, 1.0, n_participants)
psi_values = np.random.uniform(0, 1.0, n_participants)
ei_values = np.random.uniform(0, 1.0, n_participants)
ltmi_values = np.random.uniform(0, 1.0, n_participants)

# Create DataFrame with all columns
data = {
    'Participant_ID': [f'P{i+1:03d}' for i in range(n_participants)],
    'Group': np.random.choice(['Control', 'Experimental'], n_participants),
    'Session': np.random.choice([1, 2, 3], n_participants),
    'U_S': u_s_values,      # Normalized Understanding
    'D_S': d_s_values,      # Normalized Debugging
    'C_S': c_s_values,      # Normalized Completion
    'PSI': psi_values,      # Problem Solving Index
    'EI': ei_values,        # Emotion Index
    'LTMI': ltmi_values     # Long-Term Memory Index
}

df = pd.DataFrame(data)

# Save to Excel
output_file = 'sample_comprehensive_data.xlsx'
df.to_excel(output_file, index=False, sheet_name='Data')

print(f"✓ Comprehensive sample data file created: {output_file}")
print(f"  Participants: {n_participants}")
print(f"  Columns: {', '.join(df.columns.tolist())}")
print(f"\nDataFrame preview:")
print(df.head(10))
print(f"\nTechnical indices:")
print(f"  U_S range: [{df['U_S'].min():.4f}, {df['U_S'].max():.4f}]")
print(f"  D_S range: [{df['D_S'].min():.4f}, {df['D_S'].max():.4f}]")
print(f"  C_S range: [{df['C_S'].min():.4f}, {df['C_S'].max():.4f}]")
print(f"\nNon-Technical indices:")
print(f"  PSI range: [{df['PSI'].min():.4f}, {df['PSI'].max():.4f}]")
print(f"  EI range: [{df['EI'].min():.4f}, {df['EI'].max():.4f}]")
print(f"  LTMI range: [{df['LTMI'].min():.4f}, {df['LTMI'].max():.4f}]")
