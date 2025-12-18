# cipher.py

def reverse_text(text: str, decrypt: bool = False) -> str:
    """Инверсия текста (симметричная операция)."""
    return text[::-1]

def swap_adjacent(text: str, decrypt: bool = False) -> str:
    """Обмен соседних символов (симметричная операция)."""
    result = ""
    for i in range(0, len(text) - 1, 2):
        result += text[i + 1] + text[i]
    if len(text) % 2:
        result += text[-1]
    return result

def shift_chars(text: str, decrypt: bool = False, base_shift: int = 1) -> str:
    """Сдвиг символов на base_shift позиций."""
    shift = -base_shift if decrypt else base_shift
    return ''.join(chr(ord(c) + shift) for c in text)


def shift_by_position(text: str, decrypt: bool = False, base: int = 33) -> str:
    """Сдвиг по номеру позиции (с циклом по модулю base)."""
    result = ""
    p = 0
    for c in text:
        shift = -p if decrypt else p
        result += chr(ord(c) + shift)
        p = (p + 1) % base
    return result



# Технический реестр: идентификатор → функция
ALGORITHMS = {
    "reverse": reverse_text,
    "swap_adjacent": swap_adjacent,
    "shift_by_one": shift_chars,
    "shift_by_position": shift_by_position,
}

# Отображение для интерфейса: идентификатор → русское название
ALGORITHM_NAMES = {
    "reverse": "Инверсия текста",
    "swap_adjacent": "Обмен соседних символов",
    "shift_by_one": "Сдвиг каждого символа на 1",
    "shift_by_position": "Сдвиг по позиции (модуль 33)",
}
