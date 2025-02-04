# Selenium Python Example

## Articles written about this project

## Project Setup

* Clone the project
* Navigate to the project directory

* Install pytest-html-reporter by running the following command:

```
pip install pytest-html-reporter
```

* Install Selenium by running the following command:

```
pip install selenium
```

* Install requirements (dependencies) by running the following command:

```
pip install -r requirements.txt 
```

## Running Tests with report

```
python -m pytest tests_ui_layout/ --html-report=./reports
```

When no browser was selected then chromium will be used.

* Run tests:

```
pytest
```

## Viewing Test Results

* View results locally by navigate to the reports folder under the main folder of the project


## Viewing Allure Test Results
Open the code folder

* Run in Terminal:

```
allure serve
```

## View Help And Custom CLI Options

```
pytest --help
```