
def delet(s, pos):
    """
    Удаление буквы из слова, заданной номером позиции

    :param s: строка, из которой удаляется символ
    :param pos: позиция символа в удаляемой строке
    :return: строка, с удаленным символом
    """
    if (pos < 0) or (pos >= len(s)):
        return s

    return s[:pos] + s[pos + 1:]


s = "0123456789"
s2 = delet(s, 4)
print("s = ", s)
print("s2 = ", s2)
