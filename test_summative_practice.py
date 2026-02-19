from summative_practice import word_frequency, flatten_list, group_by_key, top_n, merge_dicts


def test_word_frequency():
    assert word_frequency("Hello hello world!") == {"hello": 2, "world": 1}
    assert word_frequency("Python is great. Python is powerful.") == {
        "python": 2,
        "is": 2,
        "great": 1,
        "powerful": 1
    }
    assert word_frequency("") == {}


def test_flatten_list():
    assert flatten_list([1, [2, [3, 4], 5]]) == [1, 2, 3, 4, 5]
    assert flatten_list([]) == []
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([[[]]]) == []


def test_group_by_key():
    data = [
        {"name": "Alice", "department": "IT"},
        {"name": "Bob", "department": "HR"},
        {"name": "Charlie", "department": "IT"},
    ]

    result = group_by_key(data, "department")

    assert len(result["IT"]) == 2
    assert len(result["HR"]) == 1
    assert result["HR"][0]["name"] == "Bob"


def test_top_n():
    assert top_n([5, 1, 5, 3, 9, 9], 2) == [9, 5]
    assert top_n([1, 2, 3], 1) == [3]
    assert top_n([], 3) == []
    assert top_n([4, 4, 4], 2) == [4]


def test_merge_dicts():
    assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 3}
    assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts({}, {"x": 5}) == {"x": 5}


