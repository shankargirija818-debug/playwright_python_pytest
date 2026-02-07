# Playwright Python Pytest Automation

This project automates UI testing for Flipkart using Playwright and Pytest.

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* [Optional] Virtual Environment

### Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/playwright_python_pytest.git](https://github.com/your-username/playwright_python_pytest.git)

##### Architecture ##########
'''
   project_root/
│
├── conftest.py                # Fixtures for browser setup
├── requirements.txt           # Dependencies
├── pytest.ini                 # Pytest configuration
├── screenshots/               # Failures storage
│
├── utils/
│   ├── driver_actions.py      # Utility class for all UI actions
│   └── logger.py              # Custom logging
│
├── pages/
│   ├── base_page.py           # Common page methods
│   ├── login_page.py          # Flipkart Login logic
│   └── cart_page.py           # Cart & Search logic
│
└── tests/
    ├── test_base.py           # Base Test class
    └── test_flipkart.py       # Actual test cases
   
'''

"""

       Goal:	               Command:
Stop instantly on fail:	    pytest -x
Stop after 3 fails :	       pytest --maxfail=3
Filter by name	:            pytest -k "my_function_name"
Only run previous fails :	 pytest --lf
Run all, but fails first :	 pytest --ff
Clear the cache : 	       pytest --cache-clear


"""