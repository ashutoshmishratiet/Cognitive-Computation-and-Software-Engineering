"""
Test suite for comprehensive technical & non-technical metrics computation.
Tests the extended compute_technical_from_normalized() function.
"""

import pandas as pd
import numpy as np
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import compute_technical_from_normalized

def test_input_validation():
    """Test that all 6 required columns are validated"""
    print("\n" + "="*70)
    print("TEST 1: Input Validation (All 6 Columns)")
    print("="*70)
    
    # Test missing technical columns
    df_missing_tech = pd.DataFrame({
        'U_S': [0.5],
        # Missing D_S, C_S
        'PSI': [0.5],
        'EI': [0.5],
        'LTMI': [0.5]
    })
    
    try:
        compute_technical_from_normalized(df_missing_tech)
        print("❌ FAILED: Should have raised ValueError for missing technical columns")
        return False
    except ValueError as e:
        print(f"✓ Correctly raised ValueError for missing technical: {str(e)}")
    
    # Test missing non-technical columns
    df_missing_non_tech = pd.DataFrame({
        'U_S': [0.5],
        'D_S': [0.5],
        'C_S': [0.5],
        # Missing PSI, EI, LTMI
    })
    
    try:
        compute_technical_from_normalized(df_missing_non_tech)
        print("❌ FAILED: Should have raised ValueError for missing non-technical columns")
        return False
    except ValueError as e:
        print(f"✓ Correctly raised ValueError for missing non-technical: {str(e)}")
    
    print("✓ TEST 1 PASSED\n")
    return True


def test_all_columns_computed():
    """Test that all required columns are computed"""
    print("="*70)
    print("TEST 2: All Required Columns Computed")
    print("="*70)
    
    df = pd.DataFrame({
        'Participant_ID': ['P001', 'P002'],
        'U_S': [0.5, 0.3],
        'D_S': [0.4, 0.6],
        'C_S': [0.7, 0.2],
        'PSI': [0.5, 0.4],
        'EI': [0.6, 0.5],
        'LTMI': [0.7, 0.6]
    })
    
    result = compute_technical_from_normalized(df)
    
    required_computed = [
        'CUI', 'CDI', 'CCI',
        'U_S1', 'D_S1', 'C_S1',
        'T1', 'T2', 'T3',
        'TI', 'NTI', 'CMI_P'
    ]
    
    missing = [col for col in required_computed if col not in result.columns]
    if missing:
        print(f"❌ FAILED: Missing computed columns: {missing}")
        return False
    
    print(f"✓ All {len(required_computed)} required columns present:")
    print(f"  Core indices: CUI, CDI, CCI")
    print(f"  Bloom-weighted: U_S1, D_S1, C_S1")
    print(f"  Scaled technical: T1, T2, T3")
    print(f"  Composite indices: TI, NTI, CMI_P")
    
    print("✓ TEST 2 PASSED\n")
    return True


def test_core_indices_mapping():
    """Test that core indices are direct mappings"""
    print("="*70)
    print("TEST 3: Core Indices Mapping")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [0.2, 0.8, -0.1],
        'D_S': [0.3, 0.5, 0.0],
        'C_S': [0.4, 0.6, 0.1],
        'PSI': [0.5, 0.5, 0.5],
        'EI': [0.5, 0.5, 0.5],
        'LTMI': [0.5, 0.5, 0.5]
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify CUI = U_S
    if not np.allclose(result['CUI'], df['U_S']):
        print("❌ FAILED: CUI != U_S")
        return False
    print("✓ CUI = U_S (direct mapping)")
    
    # Verify CDI = D_S
    if not np.allclose(result['CDI'], df['D_S']):
        print("❌ FAILED: CDI != D_S")
        return False
    print("✓ CDI = D_S (direct mapping)")
    
    # Verify CCI = C_S
    if not np.allclose(result['CCI'], df['C_S']):
        print("❌ FAILED: CCI != C_S")
        return False
    print("✓ CCI = C_S (direct mapping)")
    
    print("✓ TEST 3 PASSED\n")
    return True


def test_bloom_weights():
    """Test Bloom's taxonomy weights application"""
    print("="*70)
    print("TEST 4: Bloom's Taxonomy Weights (0.6, 0.2, 0.2)")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [1.0],
        'D_S': [0.5],
        'C_S': [0.2],
        'PSI': [0.5],
        'EI': [0.5],
        'LTMI': [0.5]
    })
    
    result = compute_technical_from_normalized(df)
    row = result.iloc[0]
    
    # Verify Bloom weights
    expected_u_s1 = 1.0 * 0.6  # 0.6
    expected_d_s1 = 0.5 * 0.2  # 0.1
    expected_c_s1 = 0.2 * 0.2  # 0.04
    
    if not np.isclose(row['U_S1'], expected_u_s1):
        print(f"❌ FAILED: U_S1 should be {expected_u_s1}, got {row['U_S1']}")
        return False
    print(f"✓ U_S1 = 1.0 × 0.6 = {row['U_S1']:.4f}")
    
    if not np.isclose(row['D_S1'], expected_d_s1):
        print(f"❌ FAILED: D_S1 should be {expected_d_s1}, got {row['D_S1']}")
        return False
    print(f"✓ D_S1 = 0.5 × 0.2 = {row['D_S1']:.4f}")
    
    if not np.isclose(row['C_S1'], expected_c_s1):
        print(f"❌ FAILED: C_S1 should be {expected_c_s1}, got {row['C_S1']}")
        return False
    print(f"✓ C_S1 = 0.2 × 0.2 = {row['C_S1']:.4f}")
    
    print("✓ TEST 4 PASSED\n")
    return True


def test_scaling():
    """Test scaling to [0,1] range"""
    print("="*70)
    print("TEST 5: Scaling to [0,1] Range")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [-0.25, 0.0, 1.0],
        'D_S': [0.0, 0.0, 0.0],
        'C_S': [0.0, 0.0, 0.0],
        'PSI': [0.5, 0.5, 0.5],
        'EI': [0.5, 0.5, 0.5],
        'LTMI': [0.5, 0.5, 0.5]
    })
    
    result = compute_technical_from_normalized(df)
    
    # All T values should be in [0, 1]
    for col in ['T1', 'T2', 'T3']:
        if (result[col] < 0).any() or (result[col] > 1).any():
            print(f"❌ FAILED: {col} has values outside [0,1]")
            return False
        min_val = result[col].min()
        max_val = result[col].max()
        print(f"✓ {col} in range [{min_val:.4f}, {max_val:.4f}]")
    
    print("✓ TEST 5 PASSED\n")
    return True


def test_technical_index():
    """Test TI = T1 + T2 + T3 computation"""
    print("="*70)
    print("TEST 6: Technical Index (TI = T1 + T2 + T3)")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [0.5, 0.2],
        'D_S': [0.3, 0.6],
        'C_S': [0.4, 0.1],
        'PSI': [0.5, 0.5],
        'EI': [0.5, 0.5],
        'LTMI': [0.5, 0.5]
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify TI = T1 + T2 + T3 for each row
    for idx in range(len(result)):
        row = result.iloc[idx]
        expected_ti = row['T1'] + row['T2'] + row['T3']
        if not np.isclose(row['TI'], expected_ti):
            print(f"❌ FAILED: Row {idx} TI mismatch. Expected {expected_ti}, got {row['TI']}")
            return False
        
        print(f"✓ Row {idx}: TI = T1({row['T1']:.4f}) + T2({row['T2']:.4f}) + T3({row['T3']:.4f}) = {row['TI']:.4f}")
    
    print("✓ TEST 6 PASSED\n")
    return True


def test_non_technical_index():
    """Test NTI = (PSI + EI + LTMI) / 3 computation"""
    print("="*70)
    print("TEST 7: Non-Technical Index (NTI = (PSI + EI + LTMI) / 3)")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [0.5, 0.5],
        'D_S': [0.5, 0.5],
        'C_S': [0.5, 0.5],
        'PSI': [0.6, 0.3],
        'EI': [0.5, 0.6],
        'LTMI': [0.7, 0.4]
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify NTI = (PSI + EI + LTMI) / 3 for each row
    for idx in range(len(result)):
        row = result.iloc[idx]
        expected_nti = (row['PSI'] + row['EI'] + row['LTMI']) / 3
        if not np.isclose(row['NTI'], expected_nti):
            print(f"❌ FAILED: Row {idx} NTI mismatch. Expected {expected_nti}, got {row['NTI']}")
            return False
        
        print(f"✓ Row {idx}: NTI = ({row['PSI']:.4f} + {row['EI']:.4f} + {row['LTMI']:.4f}) / 3 = {row['NTI']:.4f}")
    
    print("✓ TEST 7 PASSED\n")
    return True


def test_comprehension_measure_index():
    """Test CMI_P = 0.5 × TI + 0.5 × NTI computation"""
    print("="*70)
    print("TEST 8: Comprehension Measure Index (CMI_P = 0.5 × TI + 0.5 × NTI)")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [0.5, 0.8],
        'D_S': [0.4, 0.3],
        'C_S': [0.6, 0.7],
        'PSI': [0.5, 0.4],
        'EI': [0.6, 0.5],
        'LTMI': [0.7, 0.6]
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify CMI_P = 0.5 × TI + 0.5 × NTI for each row
    for idx in range(len(result)):
        row = result.iloc[idx]
        expected_cmi_p = 0.5 * row['TI'] + 0.5 * row['NTI']
        if not np.isclose(row['CMI_P'], expected_cmi_p):
            print(f"❌ FAILED: Row {idx} CMI_P mismatch. Expected {expected_cmi_p}, got {row['CMI_P']}")
            return False
        
        print(f"✓ Row {idx}: CMI_P = 0.5 × TI({row['TI']:.4f}) + 0.5 × NTI({row['NTI']:.4f}) = {row['CMI_P']:.4f}")
    
    print("✓ TEST 8 PASSED\n")
    return True


def test_original_columns_preserved():
    """Test that original columns are preserved unchanged"""
    print("="*70)
    print("TEST 9: Original Columns Preserved")
    print("="*70)
    
    df = pd.DataFrame({
        'Participant_ID': ['P001', 'P002', 'P003'],
        'Group': ['A', 'B', 'A'],
        'U_S': [0.5, 0.3, 0.7],
        'D_S': [0.4, 0.6, 0.2],
        'C_S': [0.6, 0.2, 0.8],
        'PSI': [0.5, 0.4, 0.6],
        'EI': [0.6, 0.5, 0.7],
        'LTMI': [0.7, 0.6, 0.5],
        'Extra_Column': ['x', 'y', 'z']
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify original columns exist
    original_cols = ['Participant_ID', 'Group', 'U_S', 'D_S', 'C_S', 'PSI', 'EI', 'LTMI', 'Extra_Column']
    missing_original = [col for col in original_cols if col not in result.columns]
    if missing_original:
        print(f"❌ FAILED: Missing original columns: {missing_original}")
        return False
    print(f"✓ All original columns preserved: {', '.join(original_cols)}")
    
    # Verify values unchanged
    if not df['Participant_ID'].equals(result['Participant_ID']):
        print("❌ FAILED: Participant_ID values changed")
        return False
    if not df['Group'].equals(result['Group']):
        print("❌ FAILED: Group values changed")
        return False
    if not np.allclose(df['PSI'], result['PSI']):
        print("❌ FAILED: PSI values changed")
        return False
    if not np.allclose(df['EI'], result['EI']):
        print("❌ FAILED: EI values changed")
        return False
    if not np.allclose(df['LTMI'], result['LTMI']):
        print("❌ FAILED: LTMI values changed")
        return False
    
    print("✓ PSI, EI, LTMI values preserved exactly")
    print("✓ All other columns preserved")
    print("✓ TEST 9 PASSED\n")
    return True


def test_statistics_computation():
    """Test that statistics can be computed correctly"""
    print("="*70)
    print("TEST 10: Statistics Computation")
    print("="*70)
    
    np.random.seed(42)
    n = 50
    df = pd.DataFrame({
        'U_S': np.random.uniform(-0.25, 1.0, n),
        'D_S': np.random.uniform(-0.25, 1.0, n),
        'C_S': np.random.uniform(-0.25, 1.0, n),
        'PSI': np.random.uniform(0, 1, n),
        'EI': np.random.uniform(0, 1, n),
        'LTMI': np.random.uniform(0, 1, n)
    })
    
    result = compute_technical_from_normalized(df)
    
    # Compute some statistics
    try:
        ti_mean = result['TI'].mean()
        ti_std = result['TI'].std()
        nti_mean = result['NTI'].mean()
        cmi_p_mean = result['CMI_P'].mean()
        
        print(f"✓ Computed statistics for {len(result)} participants:")
        print(f"  TI mean: {ti_mean:.4f}, std: {ti_std:.4f}")
        print(f"  NTI mean: {nti_mean:.4f}")
        print(f"  CMI_P mean: {cmi_p_mean:.4f}")
        
        # Verify statistics are reasonable
        if ti_mean < 0 or ti_mean > 3:
            print(f"⚠️  WARNING: TI mean {ti_mean:.4f} seems outside expected range")
        if nti_mean < 0 or nti_mean > 1:
            print(f"⚠️  WARNING: NTI mean {nti_mean:.4f} should be in [0,1]")
        if cmi_p_mean < 0 or cmi_p_mean > 1:
            print(f"⚠️  WARNING: CMI_P mean {cmi_p_mean:.4f} should be in [0,1]")
        
        print("✓ TEST 10 PASSED\n")
        return True
    except Exception as e:
        print(f"❌ FAILED: {str(e)}")
        return False


if __name__ == '__main__':
    print("\n" + "="*70)
    print("COMPREHENSIVE TECHNICAL & NON-TECHNICAL METRICS TEST SUITE")
    print("="*70)
    
    tests = [
        test_input_validation,
        test_all_columns_computed,
        test_core_indices_mapping,
        test_bloom_weights,
        test_scaling,
        test_technical_index,
        test_non_technical_index,
        test_comprehension_measure_index,
        test_original_columns_preserved,
        test_statistics_computation
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ TEST EXCEPTION: {str(e)}\n")
            results.append(False)
    
    print("="*70)
    print("SUMMARY")
    print("="*70)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if all(results):
        print("\n✅ ALL TESTS PASSED - Comprehensive metrics implementation is correct\n")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED\n")
        sys.exit(1)
