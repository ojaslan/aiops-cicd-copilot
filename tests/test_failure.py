def test_application():
    expected = 10
    actual = 5

    assert actual == expected, (
        f"Expected {expected}, but got {actual}"
    )


if __name__ == "__main__":
    test_application()