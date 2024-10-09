import os

def total_salary(path: str):
    """
    Функція для підрахунку загальної та середньої зарплати.
    
    Parameters:
    path (str): Шлях до файлу з даними про зарплату.
    
    Returns:
    tuple: Загальна і середня зарплата, або (None, None) у разі помилки.
    """
    try:
        # Список для зберігання зарплат
        salaries = []
        
        # Зчитування з файлу
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо ім'я та зарплату
                    name, salary = line.strip().split(',')
                    salaries.append(int(salary))  # Додаємо зарплату до списку
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}. Пропустити.")

        # Обчислення загальної та середньої зарплати
        total = sum(salaries)
        count = len(salaries)
        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None

def create_salary_file(file_path: str, data: list):
    """
    Функція для створення файлу з даними про зарплату.
    
    Parameters:
    file_path (str): Шлях до файлу, який потрібно створити.
    data (list): Список рядків з даними про зарплату.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(data)

def main():
    # Шлях до файлу
    file_path = "path/to/salary_file.txt"
    
    # Дані для запису
    data = [
        "Alex Korp,3000\n",
        "Nikita Borisenko,2000\n",
        "Sitarama Raju,1000\n"
    ]
    
    # Створюємо файл
    create_salary_file(file_path, data)
    print(f"Файл {file_path} успішно створено.")

    # Приклад використання функції
    total, average = total_salary(file_path)
    if total is not None and average is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()