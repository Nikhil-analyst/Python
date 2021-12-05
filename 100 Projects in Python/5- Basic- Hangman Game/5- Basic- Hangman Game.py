import random

lives = 10
list_of_words = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
                'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
word = list((random.choice(list_of_words)).lower())
dummy_word = list(word)
word_do_not_change = list(word)

Incorect_letters = []

dashed =["_" ]* len(word)
Guessed_correctly = dashed
print('Guessed Correct: ',','.join(Guessed_correctly))

def count_lives():
    global lives
    lives -= 1
    return lives

def ask_user():
    if len(word) > 0:
        user = input("\nGuess the letter: ")
    else:
        user = "Null"
    return user

def operate():
    index = dummy_word.index(user_word)
    Guessed_correctly[index] = user_word
    dummy_word[index] = "_"
    word.remove(user_word)
    print('Word : ',','.join(Guessed_correctly))
    print(f"Incorrect words guessed: {','.join(Incorect_letters)}")

user_word = ask_user()

while lives > 1:
    if user_word in word:
        operate()
        if len(word) < 1:
            print(f"\nCongrats !!! \nyou Won with lives : {lives} 🎉")
            lives = 0
            break
        print(f"Lives: {lives}")
        user_word = ask_user()
    else:
        Incorect_letters.append(user_word)
        print(f"Sorry incorrect guess 😢😢")
        print('Word : ',','.join(Guessed_correctly))
        print(f"Incorrect words guessed: {','.join(Incorect_letters)}")
        print(f"Lives: {count_lives()}")
        user_word = ask_user()
else:
    print("\nYou Lost 😥😥")
    print('Word : ',','.join(Guessed_correctly))
    print(f"Incorrect words guessed: {','.join(Incorect_letters)}")
    print(f"The word was: {''.join(word_do_not_change)}")
