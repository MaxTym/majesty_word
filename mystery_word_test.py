from mystery_word import lettet_in_secret_word


def test_guess_check_true():
    assert lettet_in_secret_word('a', 'apple') == True

def test_guess_check_false():
    assert lettet_in_secret_word('b', 'apple') != True
