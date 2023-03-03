import os

from sievetools import *

def test_primes_15():
    assert sieve_slow(15) == [2, 3, 5, 7, 11, 13]