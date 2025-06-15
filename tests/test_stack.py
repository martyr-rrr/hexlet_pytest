import pytest
from src.hexlet_pytest.stack import Stack

def test_push_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty()
    stack.push(1)
    assert not stack.is_empty()

def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError) as e:
        stack.pop()
    assert "pop from empty stack" in str(e.value)
