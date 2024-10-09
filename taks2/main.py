
def create_cats_file(path):
    cats_data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
"""

    with open(path, 'w', encoding='utf-8') as file:
        file.write(cats_data)

def get_cats_info(path):
    cats = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')

                if len(parts) != 3:
                    continue
                
                cat_id, name, age = parts
                
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
                
    except FileNotFoundError:
        print(f"Файл по пути '{path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    return cats

# Создаем файл с данными о котах
cats_file_path = "cats_file.txt"
create_cats_file(cats_file_path)

# Получаем информацию о котах из файла
cats_info = get_cats_info(cats_file_path)
print(cats_info)