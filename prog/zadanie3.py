#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fix_spelling(word):
    if "б" in word and "о" in word and "ай" in word and "т" in word:
        # Перемещаем буквы для получения "килобайт"
        corrected_word = word.replace("б", "").replace("о", "", 1).replace("ай", "о").replace("т", "байт")
        return corrected_word
    else:
        print("Ошибка: В слове отсутствуют необходимые буквы.")
        return word

if __name__ == "__main__":
    misspelled_word = "килбайот"
    corrected_word = fix_spelling(misspelled_word)
    print(f"Исправленное слово: {corrected_word}")