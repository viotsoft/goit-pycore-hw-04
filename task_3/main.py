import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)

def print_directory_structure(path: Path, prefix: str = ""):
    # Перевірка, чи є шлях директорією
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Помилка: {path} не є дійсною директорією.")
        return
    
    # Отримуємо список всіх елементів у директорії
    entries = list(path.iterdir())
    
    for i, entry in enumerate(entries):
        # Форматування префікса для виводу
        connector = "┗" if i == len(entries) - 1 else "┣"
        print(prefix + connector + " " + (Fore.BLUE + entry.name if entry.is_dir() else Fore.GREEN + entry.name))

        # Якщо це директорія, рекурсивно викликаємо функцію
        if entry.is_dir():
            print_directory_structure(entry, prefix + " ┃ ")

def main():
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python hw03.py /шлях/до/вашої/директорії")
        return
    
    path = Path(sys.argv[1])
    print_directory_structure(path)

if __name__ == "__main__":
    main()