import requests
from bs4 import BeautifulSoup

LANGUAGES = ["Arabic", "German", "English", "Spanish",
             "French", "Hebrew", "Japanese", "Dutch",
             "Polish", "Portuguese", "Romanian",
             "Russian", "Turkish"]


def word_translations(soup, word):
    words = soup.find_all("a", class_="translation")
    try:
        assert len(words) > 1
    except AssertionError:
        return f'Unfortunately, we cannot find the translations ' \
               f'for the given word: "{word}".'
    return ", ".join([w.text.strip() for w in words[1:]])


def sent_translations(soup):
    sentences = soup.find_all("div", class_=("src ltr", "trg ltr"))
    return [s.text.strip() + "\n" if sentences.index(s) % 2 == 1 else s.text.strip() for s in sentences]
    # src_sentence = soup.find("div", class_="src").text.strip()
    # trg_sentence = soup.find("div", class_="trg").text.strip()
    # return src_sentence, trg_sentence


def main(target_lang, source_lang, word):
    url = "https://context.reverso.net/translation/{}-{}/{}".format(source_lang.lower(),
                                                                    target_lang.lower(),
                                                                    word.lower())
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    words = word_translations(soup, word)
    sentences = "\n".join(sent_translations(soup))
    return words, sentences


def save(word, output):
    with open(f"{word}.txt", "a", encoding="utf-8") as file:
        file.writelines(output)
