import os

def list_files_recursively(directory):
    try:
        # Przejdź przez zawartość katalogu
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                # Jeśli element jest plikiem, wypisz jego ścieżkę
                print(f"Plik: {item_path}")
            elif os.path.isdir(item_path):
                # Jeśli element jest katalogiem, wywołaj funkcję rekurencyjnie
                list_files_recursively(item_path)
    except PermissionError:
        print(f"Brak uprawnień do odczytu katalogu: {directory}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    directory = input("Podaj ścieżkę do katalogu, który chcesz przeszukać: ")
    if os.path.isdir(directory):
        print(f"Pliki w katalogu '{directory}':")
        list_files_recursively(directory)
    else:
        print("Podana ścieżka nie jest katalogiem.")