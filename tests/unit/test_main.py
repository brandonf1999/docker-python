#!/bin/env python3

from helloworld.main import HelloWorld

def test_hello_function():
    hw = HelloWorld()
    assert hw.hello() == "Hello, World!"

