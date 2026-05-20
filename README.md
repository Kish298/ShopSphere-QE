# ShopSphere-QE

A comprehensive Quality Engineering suite for testing and performance validation of the ShopSphere e-commerce platform. This project combines **UI automation**, **API testing**, and **performance testing** with detailed reporting and CI/CD integration.

---

## 📋 Project Overview

ShopSphere-QE is a modern test automation framework designed to ensure quality across all layers of the ShopSphere platform:

- **UI Testing**: End-to-end browser automation for user workflows
- **API Testing**: Comprehensive REST API validation and integration tests
- **Performance Testing**: Load and stress testing with k6
- **Reporting**: Detailed Allure reports with test execution metrics
- **CI/CD Ready**: Docker-based execution for continuous integration pipelines

### Key Features
✅ Parallel test execution (up to 5 workers)  
✅ Comprehensive test organization (smoke, regression, api, ui markers)  
✅ Rich HTML and Allure reports  
✅ JSON test reports for CI integration  
✅ Performance benchmarking with k6  
✅ Docker support for consistent environments  

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Language** | Python | 3.11 |
| **Test Framework** | pytest | 8.4.1 |
| **Browser Automation** | Playwright | 1.55.0 |
| **API Testing** | requests, httpx | 2.32.5, 0.28.1 |
| **Performance Testing** | k6 | 2.0.0+ |
| **Reporting** | Allure, pytest-html | 2.15.0 |
| **Parallel Execution** | pytest-xdist | 3.8.0 |
| **Data Generation** | Faker | 37.6.0 |
| **Container** | Docker | Python 3.11-slim |
| **CI Integration** | pytest-json-report, pytest-metadata | 1.5.0, 3.1.1 |

### Additional Libraries
- **pytest-base-url**: Base URL configuration for API testing
- **pytest-timeout**: Timeout management for long-running tests
- **pytest-asyncio**: Async test support
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation
- **Google APIs**: Test data integration (Sheets, Drive)

---

## 🚀 How to Run

### Prerequisites
- **Python 3.11+**
- **pip** (Python package manager)
- **k6** (for performance testing)
- **Docker** (optional, for containerized execution)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ShopSphere-QE
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   ```

5. **Configure environment variables**
   ```bash
   # Create .env file with your configuration
   cp .env.example .env  # if available
   ```

### Running Tests

#### Run All Tests
```bash
pytest
```

#### Run Specific Test Type
```bash
# UI Tests Only
pytest tests/ui

# API Tests Only
pytest tests/api

# Smoke Tests
pytest -m smoke

# Regression Tests
pytest -m regression
```

#### Run with Parallel Execution
```bash
pytest -n 5  # Run with 5 workers
```

#### Generate Reports
```bash
# Allure Report (auto-generated)
pytest --alluredir=reports

# View Allure Report
allure serve reports
```

### Performance Testing with k6

```bash
cd performance
k6 run test_posts.js
```

**k6 Test File** (`performance/test_posts.js`):
- Tests GET requests to JSONPlaceholder API
- Validates 200 status responses
- Includes 1-second sleep between requests
- Suitable for baseline load testing

### Docker Execution

Build and run tests in Docker:

```bash
# Build Docker image
docker build -t shopsphere-qe .

# Run tests in container
docker run --rm shopsphere-qe

# Run specific tests
docker run --rm shopsphere-qe pytest tests/api -m smoke

# Generate reports with volume mount
docker run --rm -v "$(pwd)/reports:/app/reports" shopsphere-qe
```

### Directory Structure
```
ShopSphere-QE/
├── tests/
│   ├── api/              # API test suites
│   ├── ui/               # UI automation tests
│   └── conftest.py       # pytest fixtures and hooks
├── performance/          # k6 performance tests
│   └── test_posts.js
├── pages/                # Page Object Models (POM)
├── core/                 # Core utilities and helpers
├── utils/                # Utility functions
├── test_data/            # Test data fixtures
├── reports/              # Test execution reports
├── requirements.txt      # Python dependencies
├── pytest.ini            # pytest configuration
├── conftest.py           # Global fixtures
├── Dockerfile            # Container configuration
└── README.md             # This file
```

---

## 📊 CI/CD Integration

### GitHub Actions Example

```yaml
name: QE Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: playwright install --with-deps
      - run: pytest -n 5 --json-report --html=reports/report.html
      - uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-reports
          path: reports/
```

### CI Screenshot Example
_(Add your CI pipeline status badge here)_

```markdown
[![Tests](https://github.com/your-repo/actions/workflows/test.yml/badge.svg)](https://github.com/your-repo/actions)
```

---

## 📈 Sample Reports

### Test Execution Report
After running tests, reports are generated in the `reports/` directory:

- **Allure Report**: Interactive HTML report with:
  - Test execution timeline
  - Pass/fail statistics
  - Test history
  - Failure analysis
  
  View with: `allure serve reports`

- **HTML Report**: `reports/report.html`
  - Summary statistics
  - Test duration metrics
  - Error stack traces

- **JSON Report**: `reports/report.json`
  - Machine-readable test results
  - Suitable for CI/CD integration

### Sample Output
```
============================= test session starts ==============================
platform win32 -- Python 3.11.x, pytest-8.4.1
collected 42 items

tests/api/test_users.py .........................                      [ 40%]
tests/ui/test_checkout.py ...................                          [ 100%]

============================== 42 passed in 2.34s ===============================
Allure report generated in: reports/
```

### Report Metrics
- **Total Tests**: Track all test cases
- **Pass Rate**: Success percentage
- **Execution Time**: Total duration per suite
- **Failure Categories**: Grouped by type
- **Flaky Tests**: Identified unstable tests

---

## 🔧 Configuration

### pytest.ini
```ini
[pytest]
addopts = -v --alluredir=reports
testpaths = tests
markers =
    smoke: critical tests
    regression: full suite
    api: api tests
    ui: ui tests
```

### Environment Variables (.env)
```
BASE_URL=https://api.shopsphere.local
API_TIMEOUT=30
HEADLESS=true
RETRY_ATTEMPTS=3
LOG_LEVEL=INFO
```

---

## 📝 Test Markers

- `@pytest.mark.smoke` - Quick sanity checks (critical functionality)
- `@pytest.mark.regression` - Full test suite
- `@pytest.mark.api` - API endpoint tests
- `@pytest.mark.ui` - User interface tests

Run specific markers:
```bash
pytest -m smoke          # Only smoke tests
pytest -m "not regression"  # Everything except regression
```

---

## 🐛 Troubleshooting

### Common Issues

**k6 not recognized:**
```bash
# Windows: Reinstall k6 with PATH option checked
# Or use full path: C:\Program Files\k6\k6.exe run test_posts.js
```

**Playwright browser installation failed:**
```bash
playwright install --with-deps
```

**Port already in use (API tests):**
- Check for running services on the configured port
- Update BASE_URL in .env

**Tests timeout:**
- Increase timeout in pytest.ini: `--timeout=60`
- Check network connectivity to test endpoints

---

## 🤝 Contributing

1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Make your changes
3. Run tests locally: `pytest`
4. Commit with clear messages
5. Push and create a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

---

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact the QE team

---

**Last Updated**: May 2026  
**Framework Version**: 1.0  
**Python Version**: 3.11
