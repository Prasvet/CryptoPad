"""
GUI‑модуль на базе Tkinter для взаимодействия с крипто‑контроллером.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from controllers.crypto_controller import CryptoController
from core.cipher import ALGORITHM_NAMES  # Импортируем русские названия из cipher.py



class TkinterApp:
    """Основное окно приложения для шифрования/дешифрования."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Криптографический инструмент")
        self.root.geometry("600x450")

        self.controller = CryptoController()
        self.algo_var = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        """Создаёт и размещает все элементы интерфейса."""
        # Заголовок
        tk.Label(
            self.root,
            text="Шифрование и дешифрование",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=10)

        # Выбор алгоритма
        tk.Label(self.root, text="Алгоритм:").grid(row=1, column=0, sticky="w", padx=10, pady=5)

        # Заполняем комбо‑бокс русскими названиями алгоритмов
        self.algo_combo = ttk.Combobox(
            self.root,
            textvariable=self.algo_var,
            values=list(ALGORITHM_NAMES.values()),  # Русские названия из cipher.py
            state="readonly",
            width=30
        )
        self.algo_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Устанавливаем первый алгоритм по умолчанию
        if ALGORITHM_NAMES:
            self.algo_var.set(list(ALGORITHM_NAMES.values())[0])

        # Поле ввода
        tk.Label(self.root, text="Исходный текст:").grid(row=2, column=0, sticky="nw", padx=10, pady=(10, 5))
        self.input_field = tk.Text(self.root, height=8, width=60)
        self.input_field.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Кнопки действий
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=15)

        tk.Button(
            btn_frame,
            text="Зашифровать",
            command=self.on_encrypt,
            bg="#4CAF50",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame,
            text="Дешифровать",
            command=self.on_decrypt,
            bg="#2196F3",
            fg="white"
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="↔ Обмен",
            command=self.swap_fields,
            bg="#9C27B0",
            fg="white"
        ).pack(side="left", padx=5)

        # Поле вывода
        tk.Label(self.root, text="Результат:").grid(row=5, column=0, sticky="nw", padx=10, pady=(10, 5))
        self.output_field = tk.Text(self.root, height=8, width=60)
        self.output_field.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")

        # Растягивание
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def on_encrypt(self):
        # Получаем выбранное русское название алгоритма
        selected_name = self.algo_var.get().strip()
        if not selected_name:
            messagebox.showwarning("Ошибка", "Выберите алгоритм!")
            return

        try:
            # Находим технический идентификатор алгоритма
            algorithm_id = next(
                key for key, name in ALGORITHM_NAMES.items()
                if name == selected_name
            )

            text = self.input_field.get("1.0", tk.END).strip()
            if not text:
                messagebox.showinfo("Информация", "Введите текст для шифрования.")
                return

            result = self.controller.encrypt(text, algorithm_id)
            self.output_field.delete("1.0", tk.END)
            self.output_field.insert("1.0", result)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось зашифровать: {e}")

    def on_decrypt(self):
        # Получаем выбранное русское название алгоритма
        selected_name = self.algo_var.get().strip()
        if not selected_name:
            messagebox.showwarning("Ошибка", "Выберите алгоритм!")
            return

        try:
            # Находим технический идентификатор алгоритма
            algorithm_id = next(
                key for key, name in ALGORITHM_NAMES.items()
                if name == selected_name
            )

            text = self.output_field.get("1.0", tk.END).strip()
            if not text:
                messagebox.showinfo("Информация", "Нет текста для дешифрования.")
                return

            result = self.controller.decrypt(text, algorithm_id)
            self.input_field.delete("1.0", tk.END)
            self.input_field.insert("1.0", result)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось дешифровать: {e}")

    def swap_fields(self):
        input_text = self.input_field.get("1.0", tk.END).strip()
        output_text = self.output_field.get("1.0", tk.END).strip()
        self.input_field.delete("1.0", tk.END)
        self.input_field.insert("1.0", output_text)
        self.output_field.delete("1.0", tk.END)
        self.output_field.insert("1.0", input_text)



def run_app():
    """Запускает приложение (включает mainloop)."""
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()


# Для прямого запуска модуля
if __name__ == "__main__":
    run_app()
