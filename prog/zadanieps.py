#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_unique_words(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        word_lower = word.lower()
        word_count[word_lower] = word_count.get(word_lower, 0) + 1

    unique_words = [word for word, count in word_count.items() if count == 1]
    print("Слова, встречающиеся по одному разу:", unique_words)

if __name__ == "__main__":
    user_sentence = input("Введите предложение: ")
    print_unique_words(user_sentence)