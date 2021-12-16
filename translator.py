import requests
from bs4 import BeautifulSoup

LANGUAGES = ["0", "Arabic", "German", "English", "Spanish", "French", "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Turkish"]


def welcome():
    print("Hello, you're welcome to the translator. Translator supports:")
    print(*[f"{LANGUAGES.index(l)}. {l}" for l in LANGUAGES[1:]], sep="\n")
    source_lang = LANGUAGES[int(input("Type the number of your language: "))].lower()
    target_lang = LANGUAGES[int(input("Type the number of a language you want to translate to or '0' to translate to all languages: "))].lower()
    word = input("Type the word you want to translate: ")
    main(target_lang, source_lang, word)


def word_translations(soup):
    # words = soup.find_all("a", class_="translation")
    # return [w.text.strip() for w in words]
    word = (soup.find_all("a", class_="translation"))[1].text.strip()
    return word


def sent_translations(soup):
    # sentences = soup.find_all("div", class_=("src ltr", "trg ltr"))
    # return [s.text.strip() for s in sentences]
    src_sentence = soup.find("div", class_="src").text.strip()
    trg_sentence = soup.find("div", class_="trg").text.strip()
    return src_sentence, trg_sentence


def main(target_lang, source_lang, word):
    if target_lang == "0":
        for k in LANGUAGES[1:]:
            if k.lower() != source_lang:
                main(k.lower(), source_lang, word)
        return
    else:
        url = "https://context.reverso.net/translation/{}-{}/{}".format(source_lang, target_lang, word)
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    target_lang = target_lang.capitalize()
    output = [f"{target_lang} Translations:\n",
              word_translations(soup),
              "\n\n",
              f"{target_lang} Example:\n",
              "\n".join(sent_translations(soup)),
              "\n\n"]
    output = "".join(output)
    save(word, output)
    print(*open(f"{word}.txt", "r").readlines(), sep="")


def save(word, output):
    with open(f"{word}.txt", "a", encoding="utf-8") as file:
        file.write(output)


welcome()
