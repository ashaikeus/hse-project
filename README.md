# Parser-Translator

A simple translating software getting input through GUI and parsing results from Context Reverso without using the API.
Has tests, docstrings and an executable build.

__Tools I used:__
- **Beautiful Soup**
- **PyQt6**
- Qt Designer

__Implemented functions:__
- GUI
- create URL based on user input
- return some of the best translations parsed
- return some of the example sentences parsed
- save results to .txt
- strip given word / sentence of punctuation and forbidden symbols to prevent saving problems

I also used urllib.parse.quote_plus to transform Unicode symbols to URLs.
