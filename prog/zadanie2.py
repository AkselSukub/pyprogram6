#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def swap_letters(word, m, n):
    if 0 <= m < len(word) and 0 <= n < len(word):
        word_list = list(word)
        word_list[m], word_list[n] = word_list[n], word_list[m]
        return ''.join(word_list)
    else:
        print("Ошибка: Неверные значения m и n.")
        return word

if __name__ == "__main__":
    input_word = input("Введите слово: ")
    index_m = int(input("Введите индекс m: "))
    index_n = int(input("Введите индекс n: "))

    result_word = swap_letters(input_word, index_m, index_n)
    print(f"Слово после замены: {result_word}")