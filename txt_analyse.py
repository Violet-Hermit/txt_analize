import re


def get_text(file):
    with open(file, 'r', encoding="utf8") as file_of_text:
        text = file_of_text.read()
        file_of_text.close()
    return text

def get_list_of_words(text):
    return re.sub(r'[!?.,;:–"\']', '', text).lower().split()

def get_count_of_words_in_text(text):
    return len(text.lower().split())

def get_count_of_chars_without_spaces():
    return sum([len(i) for i in text.split()])

def get_count_of_chars_with_spaces():
    return len(text.replace("\r","").replace("\n","").strip(" "))

def count_the_frequency_of_occurrences_of_words(text):
    words = get_list_of_words(text)
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return sort_by_frequncy(result)


def sort_by_frequncy(dict_of_words):
    sorted_dict = {}
    sorted_keys = sorted(dict_of_words, key=dict_of_words.get, reverse = True)  # [1, 3, 2]
    for w in sorted_keys:
        sorted_dict[w] = dict_of_words[w]
    print(sorted_dict)

