# typing
from typing import Callable
from flask import Flask

METHODS = ['get', 'post', 'put', 'patch', 'options', 'delete']
BASE_URL = "/"

def call_wrapper(app:Flask, validator:Callable, url:str=BASE_URL, body:dict={}, methods:list=METHODS):
    """
        Wrapper to automate testing of multiple Flask methods for expected functionality.

        Arguments:
        - app {Flask} -- The Flask app under test
        - validator {Callable(str, flask.Response)} -- A function with assertions to run based on
            the passed config. Must accept two arguments, the method being tested and the response to 
            calling that method at the specified URL
        
        Keyword Arguments:
        - url {str} -- The URL to call with all passed methods. Defaults to "/"
        - body {dict} -- The request body to call with all passed methods. Defaults to {}
        - methods {List[str]} -- The methods to call the url with, defaults to :METHODS:

        Raises:
        - AssertionError: If an assertion in the passed validator fails
    """
    
    # Invoke a test client
    with app.test_client() as c:
        # For each specified method
        for method in methods:
            # Call the method at the specified url with the passed body
            rv = getattr(c, method)(url, json=body)
            # Call the validator with the method and result to run assertions on the Request/Response
            validator(method, rv)
