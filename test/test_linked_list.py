from src.linked_list import Node, LinkedList


def test_node_creation():
    node = Node("Song A")

    assert node.data == "Song A"
    assert node.next is None

def test_empty_linked_list():
    linked_list = LinkedList()

    assert linked_list.head is None

def test_append():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song B"
    assert linked_list.head.next.next.data == "Song C"
    assert linked_list.head.next.next.next is None

def test_prepend():
    linked_list = LinkedList()

    linked_list.append("Song B")
    linked_list.append("Song C")
    linked_list.prepend("Song A")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song B"
    assert linked_list.head.next.next.data == "Song C"
    assert linked_list.head.next.next.next is None

def test_insert_middle():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song D")

    linked_list.insert(2, "Song C")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song B"
    assert linked_list.head.next.next.data == "Song C"
    assert linked_list.head.next.next.next.data == "Song D"
    assert linked_list.head.next.next.next.next is None


def test_insert_at_beginning():
    linked_list = LinkedList()

    linked_list.append("Song B")
    linked_list.append("Song C")

    linked_list.insert(0, "Song A")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song B"
    assert linked_list.head.next.next.data == "Song C"


def test_insert_invalid_index():
    linked_list = LinkedList()

    linked_list.append("Song A")

    try:
        linked_list.insert(5, "Song B")
        assert False
    except IndexError:
        assert True

def test_remove_middle():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    linked_list.remove("Song B")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song C"
    assert linked_list.head.next.next is None


def test_remove_first():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")

    linked_list.remove("Song A")

    assert linked_list.head.data == "Song B"
    assert linked_list.head.next is None


def test_remove_last():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    linked_list.remove("Song C")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next.data == "Song B"
    assert linked_list.head.next.next is None


def test_remove_missing_data():
    linked_list = LinkedList()

    linked_list.append("Song A")

    try:
        linked_list.remove("Song B")
        assert False
    except ValueError:
        assert True

def test_find_existing_data():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    node = linked_list.find("Song B")

    assert node is not None
    assert node.data == "Song B"


def test_find_missing_data():
    linked_list = LinkedList()

    linked_list.append("Song A")

    node = linked_list.find("Song B")

    assert node is None


def test_to_list():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    assert linked_list.to_list() == ["Song A", "Song B", "Song C"]


def test_to_list_empty():
    linked_list = LinkedList()

    assert linked_list.to_list() == []

def test_len_empty():
    linked_list = LinkedList()

    assert len(linked_list) == 0


def test_len_with_nodes():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song C")

    assert len(linked_list) == 3


def test_is_empty():
    linked_list = LinkedList()

    assert linked_list.is_empty() is True

    linked_list.append("Song A")

    assert linked_list.is_empty() is False


def test_is_empty_after_removing_last_node():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.remove("Song A")

    assert linked_list.is_empty() is True

def test_insert_into_empty_list():
    linked_list = LinkedList()

    linked_list.insert(0, "Song A")

    assert linked_list.head.data == "Song A"
    assert linked_list.head.next is None


def test_remove_from_empty_list():
    linked_list = LinkedList()

    try:
        linked_list.remove("Song A")
        assert False
    except ValueError:
        assert True


def test_insert_negative_index():
    linked_list = LinkedList()

    try:
        linked_list.insert(-1, "Song A")
        assert False
    except IndexError:
        assert True


def test_duplicate_values():
    linked_list = LinkedList()

    linked_list.append("Song A")
    linked_list.append("Song B")
    linked_list.append("Song A")

    linked_list.remove("Song A")

    assert linked_list.to_list() == ["Song B", "Song A"]
