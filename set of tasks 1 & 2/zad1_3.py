import os

def remove_words_from_file(file_path, words_to_remove, output_file):
    try:
        # Sprawdzenie, czy plik istnieje
        if not os.path.isfile(file_path):
            print("Podany plik nie istnieje.")
            return
        
        # Odczytanie zawartości pliku
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Usunięcie wybranych słów
        for word in words_to_remove:
            content = content.replace(word, "")
        
        # Zapisanie zmodyfikowanego tekstu do nowego pliku
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Przefiltrowany tekst został zapisany do pliku: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    # Pobranie ścieżki pliku wejściowego
    input_file = input("Podaj ścieżkę do pliku wejściowego: ")
    
    # Pobranie słów do usunięcia
    words = input("Podaj słowa do usunięcia, oddzielając je spacją: ").split()
    
    # Ścieżka do pliku wynikowego
    output_file = input("Podaj ścieżkę do pliku wynikowego (np. wynik.txt): ")
    
    remove_words_from_file(input_file, words, output_file)