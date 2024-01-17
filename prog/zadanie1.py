#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    input_sentence = input("Введите предложение: ")
    word_count = count_words(input_sentence)
    print(f"Количество слов в предложении: {word_count}")