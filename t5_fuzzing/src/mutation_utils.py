import random
import string


def insert_random_character(s: str) -> str:
    if s != "":
        randomIndex = getRandomIndex(s)
        return s[:randomIndex] + getRandomChar() + s[randomIndex:]
    else:
        return getRandomChar()


def delete_random_character(s: str) -> str:
    if s != "":
        randomIndex = getRandomIndex(s)
        return s[:randomIndex] + s[randomIndex + 1:]
    else:
        return s


def flip_random_character(s: str) -> str:
    if s != "":
        modifiedCharIndex = getRandomIndex(s)
        return s[:modifiedCharIndex] + getRandomChar() + s[modifiedCharIndex + 1:]
    else:
        return s

def getRandomIndex(s: str):
    return random.randint(0, len(s))
def getRandomChar():
    characters = string.ascii_letters + string.digits + '''!()-[]{};:,<>.?@#$%^&*_~'''
    return random.choice(characters)