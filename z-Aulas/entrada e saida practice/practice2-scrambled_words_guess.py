import random


with open("animais.txt", "r") as file:
    words = file.read().split("\n")


word_of_choice = random.choice(words)

scrambled_word = "".join(random.sample(word_of_choice, len(word_of_choice)))

guess_word = ""
number_of_try = 0

while guess_word != word_of_choice and number_of_try <= 3:
    guess_word = input(
        f"[tentativas: {number_of_try}/3] Arrume a palavra { scrambled_word }: "
    )
    number_of_try += 1

if number_of_try <= 3:
    print(f"Você acertou, a palavra certa é: {word_of_choice}")
else:
    print(f"Acabaram suas chances, a palavra certa é: {word_of_choice}")
