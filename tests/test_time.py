

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../src")
import src.time_print


def test_time_now_should_not_throw():
      src.time_print.return_date() 
    

def test_hello():
    return "Hello"