# Selenium Test Automation with GitHub Actions

[![Selenium Tests](https://github.com/lamaizi1/selenium-testing/actions/workflows/selenium.yml/badge.svg)](https://github.com/lamaizi1/selenium-testing/actions/workflows/selenium.yml)

![GitHub Actions](https://github.com/lamaizi1/selenium-testing/actions/workflows/selenium.yml/badge.svg)

## Overview

This project demonstrates the automation of functional web tests using **Python**, **Selenium WebDriver**, and **pytest**.

The project follows QA automation best practices by integrating:

* Selenium WebDriver
* pytest
* Page Object Model (POM)
* HTML test reports
* GitHub Actions CI/CD
* Automatic WebDriver management

Every push to the **main** branch automatically triggers the execution of the test suite using GitHub Actions.

---

## Technologies

* Python 3.12
* Selenium WebDriver
* pytest
* pytest-html
* webdriver-manager
* Git
* GitHub Actions

---

## Project Structure

```text
selenium-testing/
│
├── .github/
│   └── workflows/
│       └── selenium.yml
│
├── pages/
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_logout.py
│   └── test_add_to_cart.py
│
├── utils/
│   └── screenshot.py
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/lamaizi1/selenium-testing.git
```

Go to the project directory

```bash
cd selenium-testing
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run all tests

```bash
pytest
```

Generate HTML report

```bash
pytest --html=report.html --self-contained-html
```

---

## Continuous Integration

The project includes a GitHub Actions workflow that automatically:

* installs Python
* installs Google Chrome
* installs project dependencies
* executes Selenium tests
* generates an HTML report
* uploads the report as a workflow artifact

---

## Test Scenarios

* Login with valid credentials
* Logout
* Add product to cart
* Functional validation using assertions

---

## HTML Test Report

An HTML report is automatically generated after each execution.

Example:

```
report.html
```
## Test Report

![Report](assets/report.png)

The report is also available as a GitHub Actions Artifact after each workflow execution.

---

## Author

Soukaina Lamaizi

Computer Engineer | DevOps & Test Automation Engineer
