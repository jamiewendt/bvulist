
import pytest

L = bvulist()
L.append(2)
L.prepend(1) #

L.pop()
x = L.pop_back() #
y = L.pop_front() #


TEST_NUM = 1

@pytest.fixture
def newlist():
    L = bvulist()
    L.append(2)
    L.append(5)
    org_length = len(L)
    yield L
    yield org_length

@pytest.fixture
def emptylist():
    L = bvulist()
    yield L



def test_prepend(newlist, org_length):
    newlist.prepend(TEST_NUM)
    assert newlist[0] == TEST_NUM
    assert len(newlist) == org_length + 1


def test_pop_back(newlist, org_length):
    new_back = newlist[len(newlist)-2]
    newlist.pop_back()
    assert newlist[-1] == new_back
    assert len(newlist) == org_length - 1

def test_pop_front(newlist, org_length):
    new_front = newlist[1]
    newlist.pop_front()
    assert newlist[0] == new_front
    assert len(newlist) == org_length - 1
