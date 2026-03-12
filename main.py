import random


def prompt_int(prompt: str) -> int:
    while True:
        try:
            raw = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            raise SystemExit("\nИгра завершена.")
        try:
            return int(raw)
        except ValueError:
            print("Введите целое число.")


def main() -> None:
    secret = random.randint(1, 100)
    attempts = 0

    print("Игра: Угадай число")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = prompt_int("Ваш вариант: ")
        attempts += 1

        if guess < secret:
            print("Больше")
        elif guess > secret:
            print("Меньше")
        else:
            print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
            break


if __name__ == "__main__":
    main()

