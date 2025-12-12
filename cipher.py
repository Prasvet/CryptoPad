def reverse_text(text):
    """Инвертировать текст (алгоритм 0)."""
    return text[::-1]

def swap_adjacent(text) -> str:
    """Замена с соседней буквой (алгоритм 1)."""
    result = ""
    for i in range(0, len(text) - 1, 2):
        result += text[i + 1] + text[i]
    if len(text) % 2:
        result += text[-1]
    return result

def shift_by_one(text, shift=1):
    """Сдвиг символов на 1 (алгоритм 2)."""
    return ''.join(chr(ord(c) + shift) for c in text)

def shift_by_position(text, base=33):
    """Сдвиг на позицию (алгоритм 3)."""
    result = ""
    p = 0
    for c in text:
        result += chr(ord(c) + p)
        p = (p + 1) % base
    return result


def unshift_by_one(text, shift=1):
    """
    Функции дешифрования (обратные операции)
    """
    return ''.join(chr(ord(c) - shift) for c in text)

def unshift_by_position(text, base=33):
    """
    Расшифровывает текст, сдвигая каждый символ назад на величину,
    равную его позиции в строке (с циклом по модулю base).
    """
    result = ""
    p = 0
    for c in text:
        result += chr(ord(c) - p)
        p = (p + 1) % base
    return result

if __name__ == '__main__':
    pass