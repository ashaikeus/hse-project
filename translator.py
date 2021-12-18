import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

LANGUAGES = ["Arabic", "German", "English", "Spanish",
             "French", "Hebrew", "Japanese", "Dutch",
             "Polish", "Portuguese", "Romanian",
             "Russian", "Turkish"]


def main(target_lang, source_lang, word):
    """
    Составляет URL страницы и парсит её.
    Возвращает список слов и примеров их использования в предложении.

    Параметры:
        target_lang (str): язык, на который нужно перевести
        source_lang (str): язык, с которого переводят
        word (str): слово(сочетание), которое нужно перевести
    """

    try:
        assert word_strip(word)
    except AssertionError:
        return f"{word} is not a valid word.", f"{word} is not a valid word."
    try:
        assert target_lang != source_lang
    except AssertionError:
        return ("Please select two different languages.",
                "Please select two different languages.")
    word = word_strip(word)
    safe_word = quote_plus(word)
    url = "https://context.reverso.net/translation/{}-{}/{}".format(
        source_lang.lower(), target_lang.lower(), safe_word.lower()
        )
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")
    words = word_translations(soup, word)
    sentences = sent_translations(soup)
    return words, sentences


def word_translations(soup, word):
    """
    Возвращает список возможных переводов выбранного слова со страницы.

    Параметры:
        soup (bs4.BeautifulSoup): контент на странице
        word (str): слово(сочетание), которое нужно перевести
    """

    words = soup.find_all("a", class_="translation")
    try:
        assert len(words) > 1
    except AssertionError:
        return f'Unfortunately, we cannot find the translations ' \
               f'for the given word: "{word}".'
    return ", ".join([w.text.strip() for w in words[1:]])


def sent_translations(soup):
    """
    Возвращает список примеров использования выбранного слова со страницы.

    Параметры:
        soup (bs4.BeautifulSoup): контент на странице
    """

    sentences = soup.find_all("div", class_=("src", "trg"))
    try:
        assert len(sentences) >= 2
    except AssertionError:
        return f'Unfortunately, we cannot find usage examples ' \
               f'for the given word.'
    return "\n".join([s.text.strip() for s in sentences])


def save(word, output):
    """
    Сохраняет результат (как переведённые слова, так и примеры предложений)
    в .txt-файл в той же директории, в которой находится программа.

    Параметры:
        word (str): слово(сочетание), которое нужно перевести
        output (list): то, что записывается в файл.
                       Формируется из данных в объектах QTextBrowser
    """

    word = word_strip(word)
    assert len(word) >= 1
    with open(f"{word}.txt", "a", encoding="utf-8") as file:
        file.writelines(output)
        return "OK"


def word_strip(word):
    """
    Оставляет в последовательности символов только буквы, цифры,
    апострофы и пробелы (во избежание проблем с сохранением файла и URL)

    Параметры:
        word (str): слово(сочетание), которое нужно перевести
    """
    return "".join([l for l in str(word) if l.isalnum() or
                    l == "'" or l == " "])
