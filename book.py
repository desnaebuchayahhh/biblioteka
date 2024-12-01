import json 
import os 

DATA_FILE = "library_data.json" 

users = { 
    "admin": {"password": "password", "role": "admin"}, 
    "user": {"password": "12345", "role": "user"},  # Изменен пароль для пользователя
} 

def load_data(): 
    if os.path.exists(DATA_FILE): 
        with open(DATA_FILE, "r") as f: 
            return json.load(f) 
    else: 
        return [] 

def save_data(data): 
    with open(DATA_FILE, "w") as f: 
        json.dump(data, f, indent=4) 

def authenticate(): 
    username = input("Введите имя пользователя: ") 
    password = input("Введите пароль: ") 
    if username in users and users[username]["password"] == password: 
        return users[username]["role"] 
    else: 
        return None 

def add_book(data): 
    title = input("Введите название книги: ") 
    author = input("Введите автора: ") 
    data.append({"title": title, "author": author}) 
    save_data(data) 
    print("Книга добавлена!") 

def delete_book(data): 
    if not data: 
        print("Библиотека пуста.") 
        return 
    for i, book in enumerate(data): 
        print(f"{i+1}. {book['title']} ({book['author']})") 
    try: 
        index = int(input("Введите номер книги для удаления: ")) - 1 
        if 0 <= index < len(data): 
            del data[index] 
            save_data(data) 
            print("Книга удалена!") 
        else: 
            print("Неверный номер книги.") 
    except ValueError: 
        print("Неверный ввод.") 

def view_books(data): 
    if not data: 
        print("Библиотека пуста.") 
        return 
    for book in data: 
        print(f"Название: {book['title']}, Автор: {book['author']}") 

def sort_books(data): 
    data.sort(key=lambda x: x['title']) 
    save_data(data) 
    print("Книги отсортированы по названию.") 

def filter_books(data): 
    author_filter = input("Введите имя автора для фильтрации: ") 
    filtered_data = [book for book in data if author_filter.lower() in book['author'].lower()] 
    if filtered_data: 
        for book in filtered_data: 
            print(f"Название: {book['title']}, Автор: {book['author']}") 
    else: 
        print("Книг по этому автору нет.") 

def main(): 
    role = authenticate() 
    if role is None: 
        print("Неверный логин или пароль.") 
        return 

    data = load_data() 

    while True: 
        print("\nМеню:") 
        print("1. Добавить книгу") 
        print("2. Удалить книгу") 
        print("3. Просмотреть книги") 
        print("4. Отсортировать книги") 
        print("5. Фильтровать книги") 
        print("6. Выход") 

        choice = input("Выберите пункт меню: ") 

        if choice == "1" and role == "admin":  # только админ может добавлять 
            add_book(data) 
        elif choice == "2" and role == "admin": # только админ может удалять 
            delete_book(data) 
        elif choice == "3": 
            view_books(data) 
        elif choice == "4" and role == "admin": # только админ может сортировать 
            sort_books(data) 
        elif choice == "5": 
            filter_books(data) 
        elif choice == "6": 
            break 
        else: 
            print("Неверный пункт меню.") 

if __name__ == "__main__":
    main()
