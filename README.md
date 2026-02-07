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
<!-- 
> Run on a specific browser :  @pytest.mark.only_browser("chromium")
> Skip test by browse :        @pytest.mark.skip_browser("firefox")

> Run with a custom browser channel like Google Chrome : pytest --browser-channel chrome
> Configure base-url:    pytest --base-url http://localhost:8080
> To generate the single-file report, run:  pytest --html=report.html --self-contained-html
> Change Log Capture Behavior: pytest --html=report.html --show-capture=no Options for --show-capture include: no, stdout, stderr, or log.
> Collapse Passed Tests: To make the report easier to read, you can force the report to open with "Passed" rows collapsed: pytest --html=report.html --collapse-seeds
> Integrating with Coverage: pytest --cov=my_app --cov-report=html --html=report.html --self-contained-html
> Generating a Separate JSON Report: pytest --html=report.html --self-contained-html --json-report --json-report-file=report.json

 -->

 <!-- 
 >  set_viewport_size: 
 page = browser.new_page()
 page.set_viewport_size({"width": 640, "height": 480})
 
  -->