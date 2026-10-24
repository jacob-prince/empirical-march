from project_name import __version__


def test_package_imports() -> None:
    assert __version__ == "0.1.0"
