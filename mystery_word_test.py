from mystery_word import lettet_in_secret_word


def guess_check_true():
    assert lettet_in_secret_word('a', 'apple') == True

def guess_check_false():
    assert lettet_in_secret_word('b', 'apple') == True
