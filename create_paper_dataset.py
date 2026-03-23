"""
Create sample dataset for paper-compliant analysis
Format: Excel file with 6 required indices (all in [0,1] scale)
- CUI: Code Understanding Index
- CDI: Code Debugging Index  
- CCI: Code Completion Index
- PSI: Problem-Solving Index
- EI: Emotion Index
- LTMI: Long-Term Memory Index
"""

import pandas as pd
import numpy as np
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)

# Number of participants
n_participants = 50

# Generate sample data with realistic distributions
# All indices in [0, 1] range
data = {
    'Participant_ID': [f'P{i+1:03d}' for i in range(n_participants)],
    'CUI': np.random.beta(7, 3, n_participants),      # Code Understanding - slightly skewed high
    'CDI': np.random.beta(6.5, 3.5, n_participants),  # Debugging - slightly skewed high
    'CCI': np.random.beta(8, 2, n_participants),      # Completion - strong skew high
    'PSI': np.random.beta(6, 4, n_participants),      # Problem-Solving - moderate
    'EI': np.random.beta(5.5, 4.5, n_participants),   # Emotion - moderate-high
    'LTMI': np.random.beta(7, 3, n_participants),     # Long-Term Memory - skew high
}

df = pd.DataFrame(data)

# Ensure all values are in [0, 1]
for col in ['CUI', 'CDI', 'CCI', 'PSI', 'EI', 'LTMI']:
    df[col] = np.clip(df[col], 0, 1)

# Save to Excel
filename = 'sample_paper_compliant_dataset.xlsx'
df.to_excel(filename, index=False, sheet_name='Data')

# Print summary
print(f"\n✓ Sample dataset created: {filename}")
print(f"  Participants: {len(df)}")
print(f"  Indices: CUI, CDI, CCI, PSI, EI, LTMI")
print(f"\nSummary Statistics:")
print(f"  CUI: {df['CUI'].mean():.4f} ± {df['CUI'].std():.4f}")
print(f"  CDI: {df['CDI'].mean():.4f} ± {df['CDI'].std():.4f}")
print(f"  CCI: {df['CCI'].mean():.4f} ± {df['CCI'].std():.4f}")
print(f"  PSI: {df['PSI'].mean():.4f} ± {df['PSI'].std():.4f}")
print(f"  EI:  {df['EI'].mean():.4f} ± {df['EI'].std():.4f}")
print(f"  LTMI: {df['LTMI'].mean():.4f} ± {df['LTMI'].std():.4f}")

# Show first few rows
print(f"\nFirst 5 participants:")
print(df.head())
