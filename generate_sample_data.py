"""
Sample Data Generator for Cognitive Performance Testing
Generates realistic data for 50+ students with cognitive metrics
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sample_data(n_students=50):
    """Generate realistic cognitive performance data for testing"""
    
    np.random.seed(42)  # For reproducibility
    
    data = {
        'Student ID': [f'STU{str(i+1).zfill(3)}' for i in range(n_students)],
        'Student Name': [f'Student {i+1}' for i in range(n_students)],
        
        # Understanding Index components (0-10 scale)
        'U_C': np.random.uniform(4, 10, n_students),  # Correct answers
        'U_W': np.random.uniform(0, 3, n_students),   # Wrong answers
        'U_NA': np.random.uniform(0, 2, n_students),  # Not attempted
        
        # Debugging Index components (0-10 scale)
        'D_C': np.random.uniform(4, 10, n_students),
        'D_W': np.random.uniform(0, 3, n_students),
        'D_NA': np.random.uniform(0, 2, n_students),
        
        # Completion Index components (0-10 scale)
        'C_C': np.random.uniform(4, 10, n_students),
        'C_W': np.random.uniform(0, 3, n_students),
        'C_NA': np.random.uniform(0, 2, n_students),
        
        # Cognitive Load metrics (0-100)
        'CL1': np.random.uniform(10, 95, n_students),
        'CL2': np.random.uniform(10, 95, n_students),
        
        # Emotion metrics (0-100)
        'Emotion_Value_Scaled': np.random.uniform(20, 100, n_students),
        
        # Problem Performance Before/After (0-100)
        'P1_B_Decimal': np.random.uniform(20, 80, n_students),
        'P1_A_Decimal': np.random.uniform(40, 95, n_students),
        'P2_B_Decimal': np.random.uniform(20, 80, n_students),
        'P2_A_Decimal': np.random.uniform(40, 95, n_students),
        'P3_B_Decimal': np.random.uniform(20, 80, n_students),
        'P3_A_Decimal': np.random.uniform(40, 95, n_students),
        'P4_B_Decimal': np.random.uniform(20, 80, n_students),
        'P4_A_Decimal': np.random.uniform(40, 95, n_students),
        'P5_B_Decimal': np.random.uniform(20, 80, n_students),
        'P5_A_Decimal': np.random.uniform(40, 95, n_students),
        'P6_B_Decimal': np.random.uniform(20, 80, n_students),
        'P6_A_Decimal': np.random.uniform(40, 95, n_students),
        'P7_B_Decimal': np.random.uniform(20, 80, n_students),
        'P7_A_Decimal': np.random.uniform(40, 95, n_students),
    }
    
    df = pd.DataFrame(data)
    
    # Round numeric columns to 2 decimal places
    numeric_cols = df.select_dtypes(include=['float64']).columns
    for col in numeric_cols:
        df[col] = df[col].round(2)
    
    return df


def main():
    """Generate and save sample data"""
    print("Generating sample cognitive performance data...")
    
    # Generate data for 50 students
    df = generate_sample_data(n_students=50)
    
    # Save to Excel file
    output_file = 'uploads/Sample_Cognitive_Data.xlsx'
    df.to_excel(output_file, index=False, sheet_name='Students')
    
    print(f"✓ Sample data generated successfully!")
    print(f"✓ File saved: {output_file}")
    print(f"✓ Total students: {len(df)}")
    print(f"✓ Total columns: {len(df.columns)}")
    print(f"\nData preview:")
    print(df.head(10))
    print(f"\nData statistics:")
    print(df.describe())


if __name__ == '__main__':
    main()
