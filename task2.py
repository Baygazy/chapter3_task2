text = input("Введите слова через пробел: ").split() # input split всегда дает список

def sortByLength(i):            # объявляем функцию и даем имя sortByLength
    return len(i)               # возвратить по длине (Начиная с малого. Всегда возвращает с меньшего до большего)

text.sort(key=sortByLength)     # у списка есть метод сорт у которого есть именованный аргумент key=function
                                # должен принимать функцию. (Нельзя указывать скобки функции внутри метода сорт)
print(text)

