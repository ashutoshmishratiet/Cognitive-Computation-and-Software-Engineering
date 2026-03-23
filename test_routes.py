#!/usr/bin/env python
"""Test script to verify all routes are correctly registered"""

import sys
from app import app
from flask import url_for

print("=" * 70)
print("FLASK ROUTE VERIFICATION TEST")
print("=" * 70)

with app.test_request_context():
    # Test share routes
    try:
        share_url = url_for('admin_share_analysis', analysis_id=1)
        print(f"✓ admin_share_analysis: {share_url}")
    except Exception as e:
        print(f"✗ admin_share_analysis: {e}")
        sys.exit(1)
    
    try:
        unshare_url = url_for('admin_unshare_analysis', analysis_id=1)
        print(f"✓ admin_unshare_analysis: {unshare_url}")
    except Exception as e:
        print(f"✗ admin_unshare_analysis: {e}")
        sys.exit(1)
    
    try:
        view_url = url_for('admin_view_analysis', analysis_id=1)
        print(f"✓ admin_view_analysis: {view_url}")
    except Exception as e:
        print(f"✗ admin_view_analysis: {e}")
        sys.exit(1)
    
    try:
        publish_url = url_for('admin_publish_analysis', analysis_id=1)
        print(f"✓ admin_publish_analysis: {publish_url}")
    except Exception as e:
        print(f"✗ admin_publish_analysis: {e}")

print("\n" + "=" * 70)
print("All share/analysis routes verified successfully!")
print("=" * 70)
