import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum():
     return Accumulator()

def test_accumulator_init(accum, accum2):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
         accum.count = 10



# So For  fixture we will use below code:

import pytest

from stuff.accum import Accumulator

"""
@pytest.fixture
def accum(scope='module'):
     yeild Accumulator() #setup part
     print("Done with the test!") #clean up part

@pytest.fixture
def accum2():
    return Accumulator()
"""

import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum():
     return Accumulator()

def test_accumulator_init(accum, accum2):
    assert accum.count == 0

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
         accum.count = 10



# So For  fixture we will use below code:

import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum(scope='module'):
     yield Accumulator() #setup part
     print("Done with the test!") #clean up part

@pytest.fixture
def accum2():
    return Accumulator()


