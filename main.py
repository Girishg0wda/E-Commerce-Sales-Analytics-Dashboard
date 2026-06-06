import subprocess
import sys

scripts = [
    "src/data_cleaning.py",
    "src/business_analysis.py",
    "src/visualizations.py",
    "src/customer_segmentation.py",
    "src/dashboard_data.py",
    "src/forecasting.py",
    "src/create_database.py",
]

for script in scripts:
    print(f"\nRunning {script}")

    result = subprocess.run(
        [sys.executable, script],
        check=True
    )

print("\nAnalytics Pipeline Completed Successfully!")