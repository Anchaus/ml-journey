from pytest import raises

from hello_cli import hello_cli


def test_default_language():
    assert hello_cli(['Alexandr']) == "Hello, Alexandr"


def test_specified_language():
    args = ['Alexandr', '-l', 'German']
    assert hello_cli(args) == 'Hallo, Alexandr'
    args[1] = '--languages'
    assert hello_cli(args) == 'Hallo, Alexandr'


def test_missed_name():
    with raises(SystemExit):
        hello_cli([])
    with raises(SystemExit):
        hello_cli(['-l', 'German'])


def test_multiple_languages():
    args = ['Alexandr', '-l', 'German', 'English', 'Indonesian']
    expected_output = (
        "Hallo, Alexandr\n"
        "Hello, Alexandr\n"
        "Hai, Alexandr"
    )
    assert hello_cli(args) == expected_output


def test_unsupported_language():
    args = ['Alexandr', '-l', 'Japanese']
    with raises(SystemExit):
        hello_cli(args)
