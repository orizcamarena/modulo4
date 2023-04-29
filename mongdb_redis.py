import redis

# Connect to Redis
redis_conn = redis.Redis(host='localhost', port=6380, db=0)


def add_word():
    word = input("Ingrese la palabra a agregar: ")
    meaning = input("Ingrese el significado: ")
    redis_conn.hset('dictionary', word, meaning)
    print(f"{word} agregada al diccionario.")


def edit_word():
    word = input("Ingrese palabra a modificar: ")
    meaning = input("Ingrese el nuevo significado de la palabra: ")
    redis_conn.hset('dictionary', word, meaning)
    print(f"{word} actualizada en el diccionario.")


def remove_word():
    word = input("Ingrese la palabra a remover: ")
    redis_conn.hdel('dictionary', word)
    print(f"{word} eliminada del diccionario.")


def search_word():
    word = input("Ingrese la palabra a buscar: ")
    meaning = redis_conn.hget('dictionary', word)
    if meaning:
        print(f"{word}: {meaning.decode()}")
    else:
        print(f"{word} no esta presente en el diccionario.")


def view_dictionary():
    words = redis_conn.hgetall('dictionary')
    if words:
        for word, meaning in words.items():
            print(f"{word.decode()}: {meaning.decode()}")
    else:
        print("El diccionario esta vacio.")


def display_menu():
    print("1. Agregar palabra")
    print("2. Editar palabra")
    print("3. Remover palabra")
    print("4. Buscar palabra")
    print("5. Ver todas las palabras")
    print("6. Salir")


while True:
    display_menu()
    choice = input("Ingrese su eleccion: ")

    if choice == '1':
        add_word()
    elif choice == '2':
        edit_word()
    elif choice == '3':
        remove_word()
    elif choice == '4':
        search_word()
    elif choice == '5':
        view_dictionary()
    elif choice == '6':
        break
    else:
        print("Eleccion no valida. Por favor, intente de nuevo.")
