import os
import re

def remove_words_with_regex(input_file, words_to_remove, output_file):
    """
    Usuwa wybrane słowa z pliku wejściowego za pomocą wyrażeń regularnych.
    
    :param input_file: Ścieżka do pliku wejściowego
    :param words_to_remove: Lista słów do usunięcia
    :param output_file: Ścieżka do pliku wynikowego
    """
    try:
        # Sprawdzenie, czy plik istnieje
        if not os.path.isfile(input_file):
            print("Podany plik nie istnieje.")
            return
        
        # Odczytanie zawartości pliku
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Utworzenie wzorca do usunięcia słów
        pattern = r'\b(' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
        
        # Usuwanie wybranych słów
        filtered_content = re.sub(pattern, '', content)
        
        # Zapisanie zmodyfikowanego tekstu do nowego pliku
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(filtered_content)
        
        print(f"Przefiltrowany tekst został zapisany do pliku: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    input_file = input("Podaj ścieżkę do pliku wejściowego: ")
    words_to_remove = input("Podaj słowa do usunięcia, oddzielając je spacją: ").split()
    output_file = input("Podaj ścieżkę do pliku wynikowego (np. wynik.txt): ")
    
    remove_words_with_regex(input_file, words_to_remove, output_file)