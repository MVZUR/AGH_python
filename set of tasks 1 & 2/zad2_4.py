class fibonacci:
    def __init__(self, steps):
        """
        Inicjalizuje iterator ciągu Fibonacciego.
        
        :param steps: Liczba wyrazów ciągu, po których rzucany jest wyjątek StopIteration.
        """
        self.steps = steps  # Liczba wyrazów ciągu do zwrócenia
        self.current_step = 0  # Licznik aktualnego wyrazu
        self.a, self.b = 0, 1  # Pierwsze dwa wyrazy ciągu

    def __iter__(self):
        """Zwraca iterator (siebie)."""
        return self

    def __next__(self):
        """Zwraca kolejny wyraz ciągu Fibonacciego."""
        if self.current_step >= self.steps:
            raise StopIteration
        self.current_step += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

# Przykład użycia
if __name__ == "__main__":
    fib = fibonacci(20)  
    for num in fib:
        print(num)
