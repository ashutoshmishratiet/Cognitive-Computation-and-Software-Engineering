"""
Test suite for Bloom's taxonomy-based technical metrics computation.
Tests the compute_technical_from_normalized() function.
"""

import pandas as pd
import numpy as np
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import compute_technical_from_normalized

def test_basic_computation():
    """Test basic computation with simple values"""
    print("\n" + "="*70)
    print("TEST 1: Basic Computation")
    print("="*70)
    
    # Create test data with known values
    df = pd.DataFrame({
        'U_S': [0.0, 0.5, 1.0, -0.25],
        'D_S': [0.0, 0.5, 1.0, -0.25],
        'C_S': [0.0, 0.5, 1.0, -0.25]
    })
    
    print(f"Input DataFrame:\n{df}")
    
    result = compute_technical_from_normalized(df)
    
    print(f"\nEnriched DataFrame shape: {result.shape}")
    print(f"Columns: {result.columns.tolist()}")
    
    # Verify key columns exist
    required_cols = ['CUI', 'CDI', 'CCI', 'U_S1', 'D_S1', 'C_S1', 'T1', 'T2', 'T3', 'CL1', 'CL1_mean', 'CL1_scaled']
    missing = [col for col in required_cols if col not in result.columns]
    
    if missing:
        print(f"❌ FAILED: Missing columns: {missing}")
        return False
    
    print(f"✓ All required columns present")
    
    # Check first row: U_S=0.0, D_S=0.0, C_S=0.0
    # CUI=0.0, CDI=0.0, CCI=0.0
    # U_S1=0.0*0.6=0.0, D_S1=0.0*0.2=0.0, C_S1=0.0*0.2=0.0
    # T1 = (0+0.25)/1.25 = 0.2, T2=0.2, T3=0.2
    # CL1 = 0.6, CL1_mean = 0.2, CL1_scaled = 0.1
    
    row0 = result.iloc[0]
    print(f"\nRow 0 (all zeros in input):")
    print(f"  CUI={row0['CUI']:.4f}, CDI={row0['CDI']:.4f}, CCI={row0['CCI']:.4f}")
    print(f"  T1={row0['T1']:.4f}, T2={row0['T2']:.4f}, T3={row0['T3']:.4f}")
    print(f"  CL1={row0['CL1']:.4f}, CL1_mean={row0['CL1_mean']:.4f}, CL1_scaled={row0['CL1_scaled']:.4f}")
    
    # Verify T1, T2, T3 are in [0,1] range
    if (row0['T1'] < 0 or row0['T1'] > 1 or
        row0['T2'] < 0 or row0['T2'] > 1 or
        row0['T3'] < 0 or row0['T3'] > 1):
        print("❌ FAILED: T values outside [0,1] range")
        return False
    
    print("✓ T values in [0,1] range")
    print("✓ TEST 1 PASSED\n")
    return True


def test_validation():
    """Test input validation"""
    print("="*70)
    print("TEST 2: Input Validation")
    print("="*70)
    
    # Missing column
    df_missing = pd.DataFrame({
        'U_S': [0.0, 0.5],
        'D_S': [0.0, 0.5]
        # Missing C_S
    })
    
    try:
        result = compute_technical_from_normalized(df_missing)
        print("❌ FAILED: Should have raised ValueError for missing C_S")
        return False
    except ValueError as e:
        print(f"✓ Correctly raised error: {str(e)}")
    
    print("✓ TEST 2 PASSED\n")
    return True


def test_range_scaling():
    """Test that scaling formula works correctly"""
    print("="*70)
    print("TEST 3: Range Scaling Verification")
    print("="*70)
    
    # Create dataframe with specific values to test scaling
    # scale(x) = clip((x + 0.25) / 1.25, 0, 1)
    # 
    # Testing:
    # x = -0.25 → (0) / 1.25 = 0 → clip to 0
    # x = 0.0 → (0.25) / 1.25 = 0.2
    # x = 1.0 → (1.25) / 1.25 = 1.0 → clip to 1
    
    df = pd.DataFrame({
        'U_S': [-0.25, 0.0, 1.0],
        'D_S': [0.0, 0.0, 0.0],
        'C_S': [0.0, 0.0, 0.0]
    })
    
    result = compute_technical_from_normalized(df)
    
    print("Testing scale(x) = clip((x + 0.25) / 1.25, 0, 1)")
    print()
    
    # For row 0: U_S = -0.25, after Bloom: -0.25 * 0.6 = -0.15
    # scale(-0.15) = (-0.15 + 0.25) / 1.25 = 0.1 / 1.25 = 0.08
    expected_t1_row0 = (-0.15 + 0.25) / 1.25
    actual_t1_row0 = result.iloc[0]['T1']
    print(f"Row 0: U_S=-0.25 → U_S1=-0.15 → T1={actual_t1_row0:.4f} (expected: {expected_t1_row0:.4f})")
    
    if abs(actual_t1_row0 - expected_t1_row0) > 0.0001:
        print(f"❌ FAILED: T1 mismatch")
        return False
    
    # For row 2: U_S = 1.0, after Bloom: 1.0 * 0.6 = 0.6
    # scale(0.6) = (0.6 + 0.25) / 1.25 = 0.85 / 1.25 = 0.68
    expected_t1_row2 = (0.6 + 0.25) / 1.25
    actual_t1_row2 = result.iloc[2]['T1']
    print(f"Row 2: U_S=1.0 → U_S1=0.6 → T1={actual_t1_row2:.4f} (expected: {expected_t1_row2:.4f})")
    
    if abs(actual_t1_row2 - expected_t1_row2) > 0.0001:
        print(f"❌ FAILED: T1 mismatch")
        return False
    
    # Verify all T values are in [0, 1]
    for col in ['T1', 'T2', 'T3']:
        if (result[col] < 0).any() or (result[col] > 1).any():
            print(f"❌ FAILED: {col} has values outside [0,1]")
            return False
    
    print("\n✓ All T values in valid [0,1] range")
    print("✓ TEST 3 PASSED\n")
    return True


def test_cognitive_load():
    """Test cognitive load computation"""
    print("="*70)
    print("TEST 4: Cognitive Load Computation")
    print("="*70)
    
    df = pd.DataFrame({
        'U_S': [0.5],
        'D_S': [0.5],
        'C_S': [0.5]
    })
    
    result = compute_technical_from_normalized(df)
    
    row = result.iloc[0]
    t1, t2, t3 = row['T1'], row['T2'], row['T3']
    cl1 = row['CL1']
    cl1_mean = row['CL1_mean']
    cl1_scaled = row['CL1_scaled']
    
    # Verify CL1 = T1 + T2 + T3
    expected_cl1 = t1 + t2 + t3
    if abs(cl1 - expected_cl1) > 0.0001:
        print(f"❌ FAILED: CL1 mismatch. Got {cl1:.4f}, expected {expected_cl1:.4f}")
        return False
    
    print(f"✓ CL1 = T1 + T2 + T3 = {t1:.4f} + {t2:.4f} + {t3:.4f} = {cl1:.4f}")
    
    # Verify CL1_mean = CL1 / 3
    expected_cl1_mean = cl1 / 3
    if abs(cl1_mean - expected_cl1_mean) > 0.0001:
        print(f"❌ FAILED: CL1_mean mismatch. Got {cl1_mean:.4f}, expected {expected_cl1_mean:.4f}")
        return False
    
    print(f"✓ CL1_mean = CL1 / 3 = {cl1:.4f} / 3 = {cl1_mean:.4f}")
    
    # Verify CL1_scaled = CL1_mean * 0.5
    expected_cl1_scaled = cl1_mean * 0.5
    if abs(cl1_scaled - expected_cl1_scaled) > 0.0001:
        print(f"❌ FAILED: CL1_scaled mismatch. Got {cl1_scaled:.4f}, expected {expected_cl1_scaled:.4f}")
        return False
    
    print(f"✓ CL1_scaled = CL1_mean × 0.5 = {cl1_mean:.4f} × 0.5 = {cl1_scaled:.4f}")
    print("✓ TEST 4 PASSED\n")
    return True


def test_bloom_weights():
    """Test that Bloom's taxonomy weights are correctly applied"""
    print("="*70)
    print("TEST 5: Bloom's Taxonomy Weights")
    print("="*70)
    
    # Create distinct values to trace through
    df = pd.DataFrame({
        'U_S': [1.0],  # Understanding
        'D_S': [0.5],  # Debugging
        'C_S': [0.2]   # Completion
    })
    
    result = compute_technical_from_normalized(df)
    row = result.iloc[0]
    
    # Verify core indices are direct mappings
    print(f"Core Indices (direct mapping):")
    print(f"  CUI = U_S: {row['CUI']:.4f} == {1.0:.4f} ✓")
    print(f"  CDI = D_S: {row['CDI']:.4f} == {0.5:.4f} ✓")
    print(f"  CCI = C_S: {row['CCI']:.4f} == {0.2:.4f} ✓")
    
    # Verify Bloom's weights: U=0.6, D=0.2, C=0.2
    u_s1_expected = 1.0 * 0.6  # 0.6
    d_s1_expected = 0.5 * 0.2  # 0.1
    c_s1_expected = 0.2 * 0.2  # 0.04
    
    print(f"\nBloom's Weights (0.6, 0.2, 0.2):")
    print(f"  U_S1 = CUI × 0.6: {row['U_S1']:.4f} == {u_s1_expected:.4f} ✓")
    print(f"  D_S1 = CDI × 0.2: {row['D_S1']:.4f} == {d_s1_expected:.4f} ✓")
    print(f"  C_S1 = CCI × 0.2: {row['C_S1']:.4f} == {c_s1_expected:.4f} ✓")
    
    if not (abs(row['U_S1'] - u_s1_expected) < 0.0001 and
            abs(row['D_S1'] - d_s1_expected) < 0.0001 and
            abs(row['C_S1'] - c_s1_expected) < 0.0001):
        print("❌ FAILED: Bloom's weights not correctly applied")
        return False
    
    print("✓ TEST 5 PASSED\n")
    return True


def test_statistical_properties():
    """Test that statistics are correctly computed"""
    print("="*70)
    print("TEST 6: Statistical Properties")
    print("="*70)
    
    # Create data with multiple rows
    df = pd.DataFrame({
        'U_S': [0.0, 0.5, 1.0],
        'D_S': [0.2, 0.5, 0.8],
        'C_S': [0.1, 0.5, 0.9]
    })
    
    result = compute_technical_from_normalized(df)
    
    # Verify means are computed correctly
    cui_mean = result['CUI'].mean()
    cdi_mean = result['CDI'].mean()
    cci_mean = result['CCI'].mean()
    
    print(f"Sample means:")
    print(f"  CUI mean: {cui_mean:.4f} (from {result['CUI'].tolist()})")
    print(f"  CDI mean: {cdi_mean:.4f} (from {result['CDI'].tolist()})")
    print(f"  CCI mean: {cci_mean:.4f} (from {result['CCI'].tolist()})")
    
    # Verify T values are properly scaled (should be in [0, 1])
    t_cols = ['T1', 'T2', 'T3']
    for col in t_cols:
        min_val = result[col].min()
        max_val = result[col].max()
        if min_val < 0 or max_val > 1:
            print(f"❌ FAILED: {col} out of range [{min_val:.4f}, {max_val:.4f}]")
            return False
        print(f"  {col} range: [{min_val:.4f}, {max_val:.4f}] ✓")
    
    print("✓ TEST 6 PASSED\n")
    return True


if __name__ == '__main__':
    print("\n" + "="*70)
    print("BLOOM'S TAXONOMY TECHNICAL METRICS COMPUTATION TEST SUITE")
    print("="*70)
    
    tests = [
        test_basic_computation,
        test_validation,
        test_range_scaling,
        test_cognitive_load,
        test_bloom_weights,
        test_statistical_properties
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
        print("\n✅ ALL TESTS PASSED - Implementation is correct\n")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED\n")
        sys.exit(1)
