import sys
import re

CONSONANT_REGEX=r'[bcdfghjklmnpqrstvwxysбвгґджзклмнпрстфхцчшщ]'

class TextAnalyzer:
  result_words = set()
  max_substring_length = 0

  def analyze_word(self, word):
    substrings = re.findall(f'{CONSONANT_REGEX}+', word, re.IGNORECASE)

    for substring in substrings:
      substring_length = len(substring)

      if substring_length < self.max_substring_length:
        continue

      if substring_length > self.max_substring_length:
        self.max_substring_length = len(substring);
        self.result_words.clear()

      self.result_words.add(word)


with open(sys.argv[1], 'r', encoding='utf-8') as file:
  file_content = file.read()

  words = re.split(r'[^\w`\']+', file_content)

  analyzer = TextAnalyzer();

  for word in words:
    analyzer.analyze_word(word)

  print(analyzer.result_words)
