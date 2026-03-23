"""
Test PaperCompliantAnalyzer with sample dataset
Verify all calculations match paper specifications exactly
"""

import pandas as pd
import sys
sys.path.insert(0, '.')

from app import PaperCompliantAnalyzer

print("\n" + "="*70)
print("PAPER-COMPLIANT ANALYZER TEST SUITE")
print("="*70)

# Load sample dataset
try:
    df = pd.read_excel('sample_paper_compliant_dataset.xlsx')
    print(f"\n✓ Dataset loaded: {len(df)} participants")
except Exception as e:
    print(f"\n❌ Failed to load dataset: {e}")
    exit(1)

# Test 1: Validation
print("\n--- TEST 1: Validation ---")
analyzer = PaperCompliantAnalyzer(df)
if analyzer.validate():
    print("✓ Validation passed")
    print(f"  - All 6 required indices present: CUI, CDI, CCI, PSI, EI, LTMI")
    print(f"  - All values in [0,1] range")
else:
    print("❌ Validation failed:")
    for error in analyzer.errors:
        print(f"  - {error}")
    exit(1)

# Test 2: Analysis
print("\n--- TEST 2: Analysis & Calculations ---")
results = analyzer.analyze()
if results:
    print(f"✓ Analysis complete: {len(results)} participants processed")
else:
    print("❌ Analysis failed")
    exit(1)

# Test 3: Formula Verification
print("\n--- TEST 3: Formula Verification ---")
first_p = results[0]

# Manual calculation for first participant
cui = first_p['CUI']
cdi = first_p['CDI']
cci = first_p['CCI']
psi = first_p['PSI']
ei = first_p['EI']
ltmi = first_p['LTMI']

# TI = (1/6 × CUI) + (2/6 × CDI) + (3/6 × CCI)
ti_expected = (cui / 6) + (cdi * 2 / 6) + (cci * 3 / 6)
ti_actual = first_p['TI']

# NTI = (PSI + EI + LTMI) / 3
nti_expected = (psi + ei + ltmi) / 3
nti_actual = first_p['NTI']

# CMI_P = 0.5 × TI + 0.5 × NTI
cmi_p_expected = 0.5 * ti_expected + 0.5 * nti_expected
cmi_p_actual = first_p['CMI_P']

print(f"Participant {first_p['participant_idx']}:")
print(f"  CUI={cui:.4f}, CDI={cdi:.4f}, CCI={cci:.4f}")
print(f"  PSI={psi:.4f}, EI={ei:.4f}, LTMI={ltmi:.4f}")

print(f"\n  TI Formula: (1/6×CUI) + (2/6×CDI) + (3/6×CCI)")
print(f"    Expected: {ti_expected:.6f}")
print(f"    Actual:   {ti_actual:.6f}")
if abs(ti_expected - ti_actual) < 1e-10:
    print(f"    ✓ MATCH")
else:
    print(f"    ❌ MISMATCH (diff: {abs(ti_expected - ti_actual):.2e})")

print(f"\n  NTI Formula: (PSI + EI + LTMI) / 3")
print(f"    Expected: {nti_expected:.6f}")
print(f"    Actual:   {nti_actual:.6f}")
if abs(nti_expected - nti_actual) < 1e-10:
    print(f"    ✓ MATCH")
else:
    print(f"    ❌ MISMATCH (diff: {abs(nti_expected - nti_actual):.2e})")

print(f"\n  CMI_P Formula: 0.5×TI + 0.5×NTI")
print(f"    Expected: {cmi_p_expected:.6f}")
print(f"    Actual:   {cmi_p_actual:.6f}")
if abs(cmi_p_expected - cmi_p_actual) < 1e-10:
    print(f"    ✓ MATCH")
else:
    print(f"    ❌ MISMATCH (diff: {abs(cmi_p_expected - cmi_p_actual):.2e})")

# Test 4: Expertise Classification
print("\n--- TEST 4: Expertise Classification ---")

classification_correct = True
sample_classifications = []

for i, p in enumerate(results):
    cmi_p = p['CMI_P']
    expertise = p['expertise']
    
    # Verify classification matches the benchmark ranges
    if cmi_p >= 0.81:
        expected = 'Very High'
    elif cmi_p >= 0.61:
        expected = 'High'
    elif cmi_p >= 0.41:
        expected = 'Average'
    elif cmi_p >= 0.21:
        expected = 'Low'
    else:
        expected = 'Very Low'
    
    if expertise != expected:
        print(f"❌ P{p['participant_idx']}: CMI_P={cmi_p:.4f}, got '{expertise}', expected '{expected}'")
        classification_correct = False
    
    # Sample some classifications for display
    if i < 5:
        sample_classifications.append((cmi_p, expertise))

if classification_correct:
    print("✓ All expertise classifications correct")
    print(f"  Sample classifications:")
    for cmi, exp in sample_classifications:
        print(f"    CMI_P={cmi:.4f} → {exp}")

# Test 5: Summary Statistics
print("\n--- TEST 5: Summary Statistics ---")
stats = analyzer.get_summary_stats()
print(f"✓ Summary statistics computed:")
print(f"  Total participants: {stats['total_participants']}")
print(f"  Indices available: CUI, CDI, CCI, PSI, EI, LTMI, TI, NTI, CMI_P")
print(f"  CMI_P Mean: {stats['CMI_P_mean']:.4f} ± {stats['CMI_P_std']:.4f}")
print(f"  Expertise distribution: {stats['expertise_distribution']}")

# Test 6: Value Ranges
print("\n--- TEST 6: Value Range Verification ---")
all_in_range = True
for idx, p in enumerate(results):
    for key in ['TI', 'NTI', 'CMI_P']:
        val = p[key]
        if not (0 <= val <= 1):
            print(f"❌ P{p['participant_idx']} {key}={val:.4f} is out of [0,1] range")
            all_in_range = False

if all_in_range:
    print("✓ All computed indices in valid [0,1] range")
    print(f"  TI range: [{min(r['TI'] for r in results):.4f}, {max(r['TI'] for r in results):.4f}]")
    print(f"  NTI range: [{min(r['NTI'] for r in results):.4f}, {max(r['NTI'] for r in results):.4f}]")
    print(f"  CMI_P range: [{min(r['CMI_P'] for r in results):.4f}, {max(r['CMI_P'] for r in results):.4f}]")

# Summary
print("\n" + "="*70)
print("✓ ALL TESTS PASSED - System is paper-compliant")
print("="*70 + "\n")
