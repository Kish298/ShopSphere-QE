import subprocess
import sys
import os
from pathlib import Path
import pytest
from core.client.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def auth_token(api_client):

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = api_client.send_request(
        "POST",
        "/login",
        payload=payload
    )

    return response.json().get("token")


def pytest_sessionfinish(session, exitstatus):
    """
    Hook to generate Allure HTML report after all tests are completed.
    This ensures that the Allure report is always generated with pass/fail results.
    """
    print("\n" + "="*70)
    print("Generating Allure Report...")
    print("="*70)
    
    allure_results_dir = Path("reports")
    allure_report_dir = Path("reports/allure-report")
    
    # Ensure the reports directory exists
    allure_results_dir.mkdir(exist_ok=True)
    
    try:
        # Determine the correct allure command based on OS
        if sys.platform == "win32":
            allure_cmd = os.path.expandvars(r"%APPDATA%\npm\allure.cmd")
        else:
            allure_cmd = "allure"
        
        # Run allure generate command to create HTML report
        cmd = [
            allure_cmd,
            "generate",
            str(allure_results_dir),
            "--clean",
            "-o",
            str(allure_report_dir)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n✓ Allure report generated successfully!")
            print(f"✓ Report location: {allure_report_dir.absolute()}")
            print(f"✓ Open report: allure open {allure_report_dir}")
        else:
            print(f"\n✗ Failed to generate Allure report")
            print(f"Error: {result.stderr}")
            print(f"\nMake sure 'allure' is installed:")
            print(f"  npm install -g allure-commandline")
            print(f"  Or: choco install allure (on Windows with Chocolatey)")
    
    except FileNotFoundError:
        print(f"\n✗ 'allure' command not found!")
        print(f"\nTo fix this, install Allure Command Line:")
        print(f"  Option 1: npm install -g allure-commandline")
        print(f"  Option 2: choco install allure (Windows with Chocolatey)")
        print(f"  Option 3: brew install allure (macOS with Homebrew)")
    
    print("="*70 + "\n")
