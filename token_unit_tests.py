import jwt
import inspect
import logging

import token_generation as g
import token_verification as v


def trace_log(message):
    # Inspect this frame's caller and its code
    func = inspect.currentframe().f_back.f_code

    # Display test result and function name, parent file and line number
    print("%s: %s in %s on line %i" % (
        message, 
        func.co_name, 
        func.co_filename, 
        func.co_firstlineno,
    ))

# Testing with correct secret
def test1():
    test_token = g.generate_token1()

    if v.verify_token1(test_token) is True:
        trace_log("Test passed")
    else:
        trace_log("Test failed")

# Testing with incorrect secret
def test2():
    test_token = g.generate_token1()

    # Will never reach this point as the 
    # verification algorithm will catch it
    if v.verify_token2(test_token) is False:
        trace_log("Test passed")
    else:
        trace_log("Test failed")

# Testing with incorrect algorithm
def test3():
    test_token = g.generate_token1()

    # Will never reach this point as the 
    # verification algorithm will catch it
    if v.verify_token3(test_token) is False:
        trace_log("Test passed")
    else:
        trace_log("Test failed")

# Testing with incorrect payload
def test4():
    test_token = g.generate_token1()

    if v.verify_token4(test_token) is False:
        trace_log("Test passed")
    else:
        trace_log("Test failed")

# Testing with expired time claim
def test5():

    # Will never reach this point as the 
    # verification algorithm will catch it
    test_token = g.generate_token5()

    if v.verify_token5(test_token) is False:
        trace_log("Test passed")
    else:
        trace_log("Test failed")
