import random

HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |   -+-
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-\\
    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-\\
    |    |
    |
    |
    |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-\\
    |    |
    |    |
    |   |
    |   |
    |
   --------------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-\\
    |    |
    |    |
    |   | |
    |   | |
    |
   --------------
    """)

WORDS = ("PYTHON", "COMPUTER", "PROGRAMMING", "DEVELOPMENT", "CODING")

word = random.choice(WORDS)
so_far = "-" * len(word)
used = []
wrong = 0

print("Добро пожаловать в игру Виселица!")
while wrong < len(HANGMAN) - 1 and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже использовали следующие буквы:\n", used)
    print("\nОтгаданное слово:\n", so_far)

    guess = input("\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Вы уже использовали эту букву, попробуйте еще раз.")
        guess = input("Введите букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1

if wrong == len(HANGMAN) - 1:
    print(HANGMAN[wrong])
    print("\nВы проиграли!")
else:
    print("\nВы выйграли!")
print("\nОтгаданное слово:", word)
input("\nНажмите Enter для выхода.")
