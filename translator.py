import requests
from bs4 import BeautifulSoup

LANGUAGES = {"1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French", "6": "Hebrew", "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese", "11": "Romanian", "12": "Russian", "13": "Turkish"}


def welcome():
    print("List of supported languages:")
    print([f"{key}. {value}" for key, value in LANGUAGES.items()], sep="\n")
    source_lang = LANGUAGES[input("number of source language: ")].lower()
    target_lang = LANGUAGES[input("number of target language: ")].lower()
    word = input("the word to translate: ")
    main(target_lang, source_lang, word)


def word_translations(soup):
    words = soup.find_all("a", class_="translation")
    return [w.text.strip() for w in words]


def sent_translations(soup):
    sentences = soup.find_all("div", class_=("src ltr", "trg ltr"))
    return [s.text.strip() for s in sentences]


def main(target_lang, source_lang, word):
    url = "https://context.reverso.net/translation/{}-{}/{}".format(source_lang, target_lang, word)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    print(f"{target_lang.capitalize()} Translations", *word_translations(soup), sep="\n", end="\n \n")
    print(f"{target_lang.capitalize()} Examples", *sent_translations(soup), sep="\n")


welcome()
