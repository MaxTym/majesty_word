import random
import os

def choose_difficulty_level():
    global random_word
    while True:
        dif_level = input("Choose a level of difficulty: \n ['E'asy, 'N'ormal, 'Hard']").lower()
        if len(dif_level) >1:
            print("One letter at the time")
        elif not dif_level.isalpha():
            continue
        elif dif_level == 'e':
            random_word = random.choice(give_me_easy_words()).lower()
            break
        elif dif_level == 'n':
            random_word = random.choice(give_me_norm_words()).lower()
            break
        elif dif_level == 'h':
            random_word = random.choice(give_me_hard_words()).lower()
            break
    return random_word

def input_check():
    good_guesses = []
    bad_guesses = []
    disp = '_'*len(random_word)
    guess_count = 8
    while '_' in disp and guess_count > 0:
        guess = input("Enter a letter: ").lower()
        if len(guess) > 1:
            print("One letter at the time")
        elif not guess.isalpha():
            print("Letters only")
        elif guess == '^q':
            break
        elif '_' not in disp:
            print("You won!!!")
            break
        elif guess in good_guesses or guess in bad_guesses:
            print("You've already tried it")
        else:
            if guess in random_word:
                print("You've got it! Attempts left: {}".format(guess_count))
                good_guesses += guess
                index = 0
                while len(random_word) > 0:
                    index = random_word.find(guess, index)
                    if index == -1:
                        break
                    disp = disp[:index] + guess + disp[(index + 1):]
                    index += 1
            else:
                guess_count -=1
                bad_guesses += guess
                print("Missed, try again. Attempts left: {}".format(guess_count))
            print(disp)
            print("Good guesses: {}".format(good_guesses))
            print("Bad guesses: {}".format(bad_guesses))
    else:
        if guess_count == 0:
            print("You are out of guesses!")
            print("The word was: {}".format(random_word))
            if play_again():
                main()
            else:
                os.system('clear')
        else:
            print("You won!!!")
            if play_again():
                main()
            else:
                os.system('clear')

def play_again():
    play_again = input("Do you want to play again?: \n ['Y'/'n']").lower()
    if play_again == 'y':
        return True

def give_me_easy_words():
    comb_list = []
    easy_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words = line.split()
            comb_list += words
        for word in comb_list:
            if len(str(word)) > 4 and len(str(word)) < 6:
                easy_words.append(word)
    return easy_words

def give_me_norm_words():
    comb_list = []
    norm_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words = line.split()
            comb_list += words
        for word in comb_list:
            if len(str(word)) > 5 and len(str(word)) < 8:
                norm_words.append(word)
    return norm_words

def give_me_hard_words():
    comb_list = []
    hard_words = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            words = line.split()
            comb_list += words
        for word in comb_list:
            if len(str(word)) > 8:
                hard_words.append(word)
    return hard_words

def main():
    os.system('clear')
    choose_difficulty_level()
    print(random_word)
    print('_'*len(random_word))
    input_check()

if __name__ == '__main__':
    main()
