from mystery_word import valid_guess, lettet_in_secret_word


def test_guess_check_true():
    assert lettet_in_secret_word('a', 'apple') == True


def test_guess_check_false():
    assert lettet_in_secret_word('b', 'apple') != True


def test_valid_input_false():
    assert valid_guess('1') != True


def test_valid_input_true():
    assert valid_guess('d') == True
