# python-htttpserver

This is an implementation of a simple server in python utilizing http.server, urllib.parse and PyJWT libraries.

### Files

* **server.py** contains the actual python server itself, with GET to retrieve the webpage and verify the JWT, as well as a POST to return the generated JWT.

* **client.html** is a barebones webpage that accepts a set of inputs and returns a JWT via ajax. It also sends the JWT through the header in a GET to verify its authenticity.

* **token_unit_tests.py** is a file containing a set of unit tests for my token generation and verification functions.

* **token_verification** contains the verification function.

* **token_generation** contains the generation function.

### How to run

Before attempting to run server.py, ensure client.html, token_verification.py and token_generation.py are in the same directory and PyJWT has been added to the path.

After starting server.py, go to http://localhost:8000/client.html where you should see the webpage displayed.
