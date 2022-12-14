# TechnicalTest

REST API to get country details of a mobile number using python FastAPI framework.

* POST Api Endpoint, secured with JWT token authentication.
* Unit test cases with pytest framework.

Steps.

  1. Install all the requirements.

  2. Import the project in vscode.

  3. Run uvicorn webserver
      python -m uvicorn main:app --reload or uvicorn main:app --reload.
   
  4. Open [http://127.0.0.1:8000/docs](http://localhost:8000/docs) in browser for swagger doc and test the api.

   5. To run test cases.
      python -m pytest or pytest
