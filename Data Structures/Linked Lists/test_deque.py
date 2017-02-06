from deque import Deque
import pytest

def test_init():
    d = Deque()
    assert d.peek_front() is None
    assert d.length() == 0
    assert d.is_empty() is True

def test_init_with_list():
    d = Deque(['A', 'B', 'C'])
    assert d.peek_front() == 'A'
    assert d.peek_back() == 'C'
    assert d.length() == 3
    assert d.is_empty() is False

def test_length():
    d = Deque()
    assert d.length() == 0
    d.enqueue_front('A')
    assert d.length() == 1
    d.enqueue_front('B')
    assert d.length() == 2
    d.dequeue_front()
    assert d.length() == 1
    d.dequeue_front()
    assert d.length() == 0

def test_peek_front():
    d = Deque()
    assert d.peek_front() is None
    d.enqueue_front('A')
    assert d.peek_front() == 'A'
    d.enqueue_front('B')
    assert d.peek_front() == 'B'
    d.dequeue_front()
    assert d.peek_front() == 'A'
    d.dequeue_front()
    assert d.peek_front() is None

def test_peek_back():
    d = Deque()
    assert d.peek_back() is None
    d.enqueue_back('A')
    assert d.peek_back() == 'A'
    d.enqueue_back('B')
    assert d.peek_back() == 'B'
    d.dequeue_back()
    assert d.peek_back() == 'A'
    d.dequeue_back()
    assert d.peek_back() is None

def test_enqueue_front():
    d = Deque()
    d.enqueue_front('A')
    assert d.peek_front() == 'A'
    assert d.length() == 1
    d.enqueue_front('B')
    assert d.peek_front() == 'B'
    assert d.length() == 2
    d.enqueue_front('C')
    assert d.peek_front() == 'C'
    assert d.length() == 3
    d.enqueue_back('D')
    assert d.peek_front() == 'C'
    assert d.is_empty() is False

def test_enqueue_back():
    d = Deque()
    d.enqueue_back('A')
    assert d.peek_back() == 'A'
    assert d.length() == 1
    d.enqueue_back('B')
    assert d.peek_back() == 'B'
    assert d.length() == 2
    d.enqueue_back('C')
    assert d.peek_back() == 'C'
    assert d.length() == 3
    d.enqueue_front('D')
    assert d.peek_back() == 'C'
    assert d.is_empty() is False

def test_dequeue_front():
    d = Deque(['A', 'B', 'C'])
    assert d.dequeue_front() == 'A'
    assert d.length() == 2
    assert d.dequeue_front() == 'B'
    assert d.length() == 1
    assert d.dequeue_front() == 'C'
    assert d.length() == 0
    assert d.is_empty() is True
    with pytest.raises(ValueError):
        assert d.dequeue_front()

def test_dequeue_back():
    d = Deque(['A', 'B', 'C'])
    assert d.dequeue_back() == 'C'
    assert d.length() == 2
    assert d.dequeue_back() == 'B'
    assert d.length() == 1
    assert d.dequeue_back() == 'A'
    assert d.length() == 0
    assert d.is_empty() is True
    with pytest.raises(ValueError):
        d.dequeue_back()
