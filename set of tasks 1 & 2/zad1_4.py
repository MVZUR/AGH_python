import os

def replace_words_in_file(input_file, word_mapping, output_file):
    """
    Zamienia słowa w pliku wejściowym na podstawie słownika mapowania.
    
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
        for old_word, new_word in word_mapping.items():
            content = content.replace(old_word, new_word)
        
        # Zapisanie zmodyfikowanego tekstu do nowego pliku
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Przekształcony tekst został zapisany do pliku: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    # Pobranie ścieżki pliku wejściowego
    input_file = input("Podaj ścieżkę do pliku wejściowego: ")
    
    # Pobranie mapowania słów od użytkownika
    print("Podaj słowa do zamiany w formacie 'klucz:wartość', oddzielając pary przecinkiem.")
    mapping_input = input("Przykład: stary:nowy,tekst:wiadomość: ")
    word_mapping = {pair.split(":")[0]: pair.split(":")[1] for pair in mapping_input.split(",")}
    
    # Ścieżka do pliku wynikowego
    output_file = input("Podaj ścieżkę do pliku wynikowego (np. wynik.txt): ")
    
    replace_words_in_file(input_file, word_mapping, output_file)