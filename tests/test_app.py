def test_app_exists():
    """
    Check that the Streamlit app file exists
    """
    import os

    assert os.path.exists("app.py")


def test_basic_calculation():
    """
    Example unit test
    """

    result = 10 + 5

    assert result == 15