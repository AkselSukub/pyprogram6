def print_unique_words(sentence):
    """
    Функция для вывода слов, встречающихся в предложении по одному разу.

    :param sentence: Входное предложение.
    """
    words = sentence.split()
    word_count = {}

    for word in words:
        # Приводим слово к нижнему регистру, чтобы исключить различие в регистре
        word_lower = word.lower()

        # Обновляем счетчик для каждого слова
        word_count[word_lower] = word_count.get(word_lower, 0) + 1

    # Выводим слова, которые встречаются только один раз
    unique_words = [word for word, count in word_count.items() if count == 1]
    print("Слова, встречающиеся по одному разу:", unique_words)

# Ввод предложения с клавиатуры
user_sentence = input("Введите предложение: ")
print_unique_words(user_sentence)