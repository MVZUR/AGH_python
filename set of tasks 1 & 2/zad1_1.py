import os

def count_files_in_directory(directory="/dev"):
    try:
        # Pobierz listę plików i katalogów w podanym katalogu
        items = os.listdir(directory)
        
        # Filtruj tylko pliki
        files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        
        # Zwróć ilość plików
        return len(files)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return 0

if __name__ == "__main__":
    directory = input("Podaj ścieżkę do katalogu (domyślnie '/dev'): ") or "/dev"
    file_count = count_files_in_directory(directory)
    print(f"Ilość plików w katalogu '{directory}': {file_count}")