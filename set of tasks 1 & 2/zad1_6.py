import os
import re

def replace_words_with_regex(input_file, word_mapping, output_file):
    """
    Zamienia wybrane słowa w pliku wejściowym na inne słowa za pomocą wyrażeń regularnych.
    
    :param input_file: Ścieżka do pliku wejściowego
    :param word_mapping: Słownik z mapowaniem słów (klucz -> wartość)
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
        
        # Zamiana słów na podstawie mapowania
        def replacer(match):
            return word_mapping[match.group(0)]
        
        # Tworzenie wzorca na podstawie kluczy w słowniku
        pattern = r'\b(' + '|'.join(re.escape(word) for word in word_mapping.keys()) + r')\b'
        
        # Zamiana słów
        replaced_content = re.sub(pattern, replacer, content)
        
        # Zapisanie zmodyfikowanego tekstu do nowego pliku
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(replaced_content)
        
        print(f"Przekształcony tekst został zapisany do pliku: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    input_file = input("Podaj ścieżkę do pliku wejściowego: ")
    print("Podaj słowa do zamiany w formacie 'klucz:wartość', oddzielając pary przecinkiem.")
    mapping_input = input("Przykład: stary:nowy,tekst:wiadomość: ")
    word_mapping = {pair.split(":")[0]: pair.split(":")[1] for pair in mapping_input.split(",")}
    output_file = input("Podaj ścieżkę do pliku wynikowego (np. wynik.txt): ")
    
    replace_words_with_regex(input_file, word_mapping, output_file)