class UpperCaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Wywołanie dekorowanej funkcji, zapisanie wyniku
        result = self.func(*args, **kwargs)
        # Zmień litery na DUŻE
        if isinstance(result, str):
            return result.upper()
        return result

# Przykład użycia
@UpperCaseDecorator
def wypisz_napis():
    return "To jest przykładowy napis."

print(wypisz_napis())
