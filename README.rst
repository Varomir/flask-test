Flask-test
=============
Example of Flask web application and test automation
======================



Install
---------------------------
For initial setup the project, type:
-------------------------------------
1) Create 'venv': "$ mkdir venv"
2) Activate 'venv': ""$ source venv/bin/activate"
3) Install all 3rd party dependecies via 'pip': "$ pip install -r requirements.txt"


Run web application
-----------------------
For start Flask web application, type:
---------------------------------------------
1) Start Flask web app: "$ python src/app.py"
2) Open in your web browser: [http://127.0.0.1:5000/api/funny](http://127.0.0.1:5000/api/funny "api/funny")



Testing
-------------------
For run tests, type:
--------------------------
1) Particular test function: "pytest -s -v tests/app_test.py::test_api_funny"
2) Particular test module: "pytest -s -v tests/app_test.py"
3) All tests in package: "pytest -s -v tests"


Changelog:
0.0.2  - Add first 'flask-test' and fixture
0.0.1  - Add first endpoints 'http://127.0.0.1:5000/api/funny'
