"""
Bluestock Mutual Fund Analytics Capstone

Master Pipeline Script

Author: Prashant Nikhare
"""

import os

print("=" * 60)
print("Bluestock Mutual Fund Analytics Pipeline Started")
print("=" * 60)

print("\nStep 1 : Data Ingestion")
os.system("python data_ingestion.py")

print("\nStep 2 : Data Cleaning")
os.system("python scripts/clean_data.py")

print("\nStep 3 : Load Data into SQLite")
os.system("python scripts/load_to_sqlite.py")

print("\nStep 4 : Fund Master Analysis")
os.system("python fund_master_analysis.py")

print("\nStep 5 : Live NAV Fetch")
os.system("python live_nav_fetch.py")

print("\nStep 6 : Recommendation System")
os.system("python scripts/recommender.py")

print("\nPipeline Completed Successfully")