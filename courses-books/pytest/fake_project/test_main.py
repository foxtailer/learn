# import os
# import sys

# script_path = os.path.realpath(__file__)
# script_dir = os.path.dirname(script_path)
# sys.path.append(script_dir)

import main

def test_a():
    assert main.a() == 'a'
def test_b():
    assert main.b() == 'b'
def test_c():
    assert main.c() == 'd'
