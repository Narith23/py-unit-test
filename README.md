
# Python Unit Test Project

This project demonstrates how to create and run unit tests in a Python project using **pytest**. It also includes functionality to generate HTML reports of the test results.

## Project Structure

```plaintext
py-unit-test/
├── app/
│   ├── core/
│   │   └── config.py    # Configuration file for the application
├── main.py              # FastAPI application entry point
├── tests/               # Folder containing test files
│   └── unit/
│       └── test_main.py  # Unit tests for the FastAPI application
```
## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` package manager

### Setup
1. Clone the repository or download the project files.
2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. The `requirements.txt` file includes:
   - `pytest`: A testing framework for Python.
   - `pytest-html`: Plugin for generating HTML reports.
   - Other dependencies as per the project requirements.

### Install dependencies:

If you do not have a `requirements.txt` file, you can create one with the following dependencies:

```plaintext
pytest==8.3.5
pytest-html==4.1.1
```

Run this command to install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Tests

To run the unit tests:

1. Open your terminal and navigate to the root directory of the project (where `main.py` is located).

2. Run the tests using `pytest`:

    ```bash
    pytest tests/unit/test_main.py
    ```

   This will run the tests in `test_main.py`.

---

## Generating Test Reports

To generate an HTML report after running the tests, use the `--html` option with `pytest`:

```bash
pytest tests/unit/test_main.py --html=report.html
```

This will generate a `report.html` file in the current directory, which you can open in any browser to view the detailed test results.

### Customize the Report

You can also customize the report using the following options:

- **Set a title for the report**:

    ```bash
    pytest tests/unit/test_main.py --html=report.html --title="My Test Report"
    ```

- **Add custom metadata (e.g., Python version, OS)**:

    ```bash
    pytest tests/unit/test_main.py --html=report.html --metadata="Python Version: 3.12" --metadata="OS: Windows"
    ```

- **Self-contained report (no external CSS)**:

    ```bash
    pytest tests/unit/test_main.py --html=report.html --self-contained-html
    ```

---

## Running Tests in Parallel

If you have many tests, you can run them in parallel to speed up the execution using the `pytest-xdist` plugin:

```bash
pip install pytest-xdist
```

Run the tests with multiple workers:

```bash
pytest -n 4 tests/unit/test_main.py --html=report.html
```

This command will run the tests across 4 parallel workers and generate a report.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
