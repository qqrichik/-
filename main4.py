import tkinter as tk
from tkinter import messagebox
import random

def guess_the_number():
    root = tk.Tk()
    root.title("Угадайка")  
    root.configure(background="#000000")  
    root.geometry("300x300")  

    # Отображение окна приветствия
    welcome_label = tk.Label(root, text="Добро пожаловать в игру 'Угадай число'!", background="#000000", foreground="#ffffff")
    instructions_label = tk.Label(root, text="Я загадал число от 1 до 100. Попробуйте угадать его!", background="#000000", foreground="#ffffff")
    welcome_label.pack()
    instructions_label.pack()

    # Создание таймера
    timer = tk.StringVar()
    timer.set("00:00")
    label_timer = tk.Label(root, textvariable=timer, background="#000000", foreground="#ffffff")
    label_timer.pack()

    # Таймер для отображения времени
    def update_time():
        minutes, seconds = map(int, timer.get().split(':'))
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        timer.set(f"{minutes:02d}:{seconds:02d}")
        root.after(1000, update_time)

    # Начинаем обновление таймера
    update_time()

    # Загадать случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0  

    # Создание кнопки для ввода числа
    entry_box = tk.Entry(root, background="#000000", foreground="#ffffff")
    entry_box.pack()

    # Функция для обработки введенного числа
    def handle_guess(event=None):
        nonlocal attempts  
        guess = entry_box.get()

        if not guess.isdigit() or not (1 <= int(guess) <= 100):
            messagebox.showerror("Неправильный формат", "Пожалуйста, введите число от 1 до 100.")
            entry_box.delete(0, tk.END)
        else:
            attempts += 1
            if int(guess) < secret_number:
                messagebox.showwarning("Слишком низко", "Слишком низко! Попробуйте еще раз.")
            elif int(guess) > secret_number:
                messagebox.showwarning("Слишком высоко", "Слишком высоко! Попробуйте еще раз.")
            else:
                messagebox.showinfo("Вы победили!", f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.\nВремя: {timer.get()}")
                root.destroy()

    # Кнопка для подтверждения введенного числа
    button = tk.Button(root, text='Подтвердить', command=handle_guess, background="#000000", foreground="#ffffff")
    button.pack()

    # Установить событие нажатия клавиши Enter
    root.bind("<Return>", handle_guess)

    # Запуск основного цикла
    root.mainloop()

if __name__ == "__main__":
    guess_the_number()