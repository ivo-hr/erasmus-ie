from wonderland import rabbit
import re

def repeat_with_comma(phrase: str):
    phrase1, phrase2 = phrase, phrase
    return phrase1 + ", " + phrase2


def the(phrase: str):
    new_phrase = repeat_with_comma(phrase)
    rabbit(new_phrase)


def down():
    phrase = "I'm late"
    match = re.search("late", phrase)
    if match:
        print("Found late!")
    the(phrase)


def main():
    down()


if __name__ == "__main__":
    main()
