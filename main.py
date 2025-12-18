#!/usr/bin/env python3
"""
Точка входа в приложение CryptoPad.
Запускает GUI на основе настройки из config.py.
"""

import sys
from config import GUI_BACKEND


def load_gui_module(backend: str):
    """Динамически импортирует и возвращает функцию запуска GUI."""
    if backend == "tkinter":
        from gui.tkinter_gui import run_app
        return run_app
    elif backend == "pyqt":
        raise NotImplementedError("PyQt backend not implemented yet")
    elif backend == "flask":
        raise NotImplementedError("Flask backend not implemented yet")
    else:
        raise ValueError(f"Unsupported GUI backend: {backend}")


def main():
    """Основная функция запуска приложения."""
    print(f"Запуск CryptoPad с GUI-бэкендом: {GUI_BACKEND}")
    try:
        run_func = load_gui_module(GUI_BACKEND)
        run_func()  # Запускаем GUI (уже содержит mainloop)
    except Exception as e:
        print(f"Ошибка при запуске GUI: {e}", file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()
