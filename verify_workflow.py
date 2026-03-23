"""
Complete workflow verification: Test the full Bloom's taxonomy pipeline
from normalized input to enriched output.
"""

import pandas as pd
import numpy as np
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import compute_technical_from_normalized

def verify_workflow():
    """Verify complete workflow from input to output"""
    
    print("\n" + "="*70)
    print("BLOOM'S TAXONOMY WORKFLOW VERIFICATION")
    print("="*70)
    
    # Create sample data
    print("\n[STEP 1] Creating sample normalized dataset...")
    np.random.seed(42)
    n = 10
    
    df_input = pd.DataFrame({
        'Participant_ID': [f'P{i+1:03d}' for i in range(n)],
        'Group': np.random.choice(['Control', 'Exp'], n),
        'U_S': np.random.uniform(-0.25, 1.0, n),
        'D_S': np.random.uniform(-0.25, 1.0, n),
        'C_S': np.random.uniform(-0.25, 1.0, n),
        'Session': np.random.randint(1, 4, n)
    })
    
    print(f"✓ Created {n} participant records")
    print(f"  Columns: {', '.join(df_input.columns.tolist())}")
    print(f"\n  Sample input (first 3 rows):")
    print(df_input[['Participant_ID', 'U_S', 'D_S', 'C_S']].head(3).to_string(index=False))
    
    # Process with compute_technical_from_normalized
    print("\n[STEP 2] Computing technical metrics...")
    try:
        df_enriched = compute_technical_from_normalized(df_input)
        print("✓ Computation successful")
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
        return False
    
    # Verify output
    print("\n[STEP 3] Verifying output structure...")
    
    required_new_cols = ['CUI', 'CDI', 'CCI', 'U_S1', 'D_S1', 'C_S1', 'T1', 'T2', 'T3', 'CL1', 'CL1_mean', 'CL1_scaled']
    missing = [col for col in required_new_cols if col not in df_enriched.columns]
    
    if missing:
        print(f"❌ FAILED: Missing columns: {missing}")
        return False
    
    print(f"✓ All {len(required_new_cols)} computed columns present")
    print(f"  Original columns: {len(df_input.columns)}")
    print(f"  Enriched columns: {len(df_enriched.columns)}")
    
    # Verify data integrity
    print("\n[STEP 4] Verifying data integrity...")
    
    # Check original data is preserved
    if not df_enriched[['Participant_ID', 'Group', 'Session']].equals(
        df_input[['Participant_ID', 'Group', 'Session']]):
        print("❌ FAILED: Original data was modified")
        return False
    print("✓ Original columns preserved")
    
    # Check normalized values are preserved
    if not np.allclose(df_enriched['U_S'], df_input['U_S']):
        print("❌ FAILED: U_S values were modified")
        return False
    if not np.allclose(df_enriched['D_S'], df_input['D_S']):
        print("❌ FAILED: D_S values were modified")
        return False
    if not np.allclose(df_enriched['C_S'], df_input['C_S']):
        print("❌ FAILED: C_S values were modified")
        return False
    print("✓ Normalized input values preserved")
    
    # Verify computations
    print("\n[STEP 5] Verifying computation accuracy...")
    
    # Check a single row manually
    row = df_enriched.iloc[0]
    
    # Manual computation
    cui = row['CUI']
    cdi = row['CDI']
    cci = row['CCI']
    
    expected_u_s1 = cui * 0.6
    expected_d_s1 = cdi * 0.2
    expected_c_s1 = cci * 0.2
    
    if not np.isclose(row['U_S1'], expected_u_s1):
        print(f"❌ FAILED: U_S1 mismatch at row 0")
        return False
    if not np.isclose(row['D_S1'], expected_d_s1):
        print(f"❌ FAILED: D_S1 mismatch at row 0")
        return False
    if not np.isclose(row['C_S1'], expected_c_s1):
        print(f"❌ FAILED: C_S1 mismatch at row 0")
        return False
    
    # Check scaling
    def scale(x):
        return np.clip((x + 0.25) / 1.25, 0, 1)
    
    expected_t1 = scale(expected_u_s1)
    expected_t2 = scale(expected_d_s1)
    expected_t3 = scale(expected_c_s1)
    
    if not np.isclose(row['T1'], expected_t1):
        print(f"❌ FAILED: T1 mismatch at row 0")
        return False
    if not np.isclose(row['T2'], expected_t2):
        print(f"❌ FAILED: T2 mismatch at row 0")
        return False
    if not np.isclose(row['T3'], expected_t3):
        print(f"❌ FAILED: T3 mismatch at row 0")
        return False
    
    # Check cognitive load
    expected_cl1 = expected_t1 + expected_t2 + expected_t3
    expected_cl1_mean = expected_cl1 / 3
    expected_cl1_scaled = expected_cl1_mean * 0.5
    
    if not np.isclose(row['CL1'], expected_cl1):
        print(f"❌ FAILED: CL1 mismatch at row 0")
        return False
    if not np.isclose(row['CL1_mean'], expected_cl1_mean):
        print(f"❌ FAILED: CL1_mean mismatch at row 0")
        return False
    if not np.isclose(row['CL1_scaled'], expected_cl1_scaled):
        print(f"❌ FAILED: CL1_scaled mismatch at row 0")
        return False
    
    print("✓ All computations verified (row 0 sample)")
    
    # Check value ranges
    print("\n[STEP 6] Verifying value ranges...")
    
    for col in ['T1', 'T2', 'T3']:
        min_val = df_enriched[col].min()
        max_val = df_enriched[col].max()
        if min_val < 0 or max_val > 1:
            print(f"❌ FAILED: {col} out of range [{min_val:.4f}, {max_val:.4f}]")
            return False
        print(f"✓ {col} in valid range [{min_val:.4f}, {max_val:.4f}]")
    
    # Check CL1_scaled range (should be [0, 1.5] max)
    cl1_scaled_max = df_enriched['CL1_scaled'].max()
    if cl1_scaled_max > 1.5:
        print(f"⚠️  CL1_scaled max is {cl1_scaled_max:.4f} (expected ≤ 1.5)")
    
    # Check statistics
    print("\n[STEP 7] Computing summary statistics...")
    
    stats = {
        'CUI_mean': df_enriched['CUI'].mean(),
        'CUI_std': df_enriched['CUI'].std(),
        'T1_mean': df_enriched['T1'].mean(),
        'T1_std': df_enriched['T1'].std(),
        'CL1_scaled_mean': df_enriched['CL1_scaled'].mean(),
        'CL1_scaled_std': df_enriched['CL1_scaled'].std()
    }
    
    print(f"✓ Statistics computed:")
    print(f"  CUI:         mean={stats['CUI_mean']:.4f}, std={stats['CUI_std']:.4f}")
    print(f"  T1:          mean={stats['T1_mean']:.4f}, std={stats['T1_std']:.4f}")
    print(f"  CL1_scaled:  mean={stats['CL1_scaled_mean']:.4f}, std={stats['CL1_scaled_std']:.4f}")
    
    # Display sample output
    print("\n[STEP 8] Sample enriched output (first 3 rows):")
    display_cols = ['Participant_ID', 'CUI', 'CDI', 'CCI', 'T1', 'T2', 'T3', 'CL1_scaled']
    print(df_enriched[display_cols].head(3).to_string(index=False))
    
    # Test Excel export
    print("\n[STEP 9] Testing Excel export...")
    try:
        test_file = 'test_enriched_output.xlsx'
        df_enriched.to_excel(test_file, index=False)
        
        if os.path.exists(test_file):
            file_size = os.path.getsize(test_file)
            print(f"✓ Excel file created successfully")
            print(f"  File: {test_file}")
            print(f"  Size: {file_size:,} bytes")
            
            # Read back and verify
            df_reloaded = pd.read_excel(test_file)
            if df_reloaded.shape == df_enriched.shape:
                print(f"✓ Re-loaded successfully ({df_reloaded.shape[0]} rows, {df_reloaded.shape[1]} cols)")
            else:
                print(f"❌ FAILED: Shape mismatch on reload")
                return False
            
            # Clean up test file
            os.remove(test_file)
        else:
            print(f"❌ FAILED: File not created")
            return False
    except Exception as e:
        print(f"❌ FAILED: Excel export error: {str(e)}")
        return False
    
    # Final summary
    print("\n" + "="*70)
    print("WORKFLOW VERIFICATION SUMMARY")
    print("="*70)
    print(f"✅ INPUT:  {n} participants with U_S, D_S, C_S")
    print(f"✅ PROCESS: Applied Bloom's weights → Scaled to [0,1] → Computed CL1")
    print(f"✅ OUTPUT: Enriched DataFrame with 12 new columns")
    print(f"✅ EXPORT: Excel file generated and validated")
    print("\n✅ COMPLETE WORKFLOW VERIFIED - SYSTEM READY FOR DEPLOYMENT\n")
    
    return True


if __name__ == '__main__':
    success = verify_workflow()
    sys.exit(0 if success else 1)
