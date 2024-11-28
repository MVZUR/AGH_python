import random

def bubble_sort(arr):
    """
    Implementacja sortowania bąbelkowego.
    """
    n = len(arr)
    for i in range(n):
        # Porównywanie sąsiednich elementów
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    """
    Implementacja sortowania szybkiego (QuickSort).
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Liczba elementów do wygenerowania
    N = int(input("Podaj liczbę elementów do wygenerowania (N): "))
    random_numbers = [random.randint(1, 1000) for _ in range(N)]
    print(f"\nWygenerowane liczby:\n{random_numbers}\n")

    # Sortowanie bąbelkowe
    bubble_sorted = bubble_sort(random_numbers.copy())
    print(f"Liczby posortowane metodą bąbelkową:\n{bubble_sorted}\n")

    # Sortowanie szybkie
    quick_sorted = quick_sort(random_numbers.copy())
    print(f"Liczby posortowane metodą QuickSort:\n{quick_sorted}\n")

    # Weryfikacja za pomocą wbudowanej funkcji sortującej
    verified_sorted = sorted(random_numbers)
    print(f"Wynik weryfikacji za pomocą funkcji sorted():\n{verified_sorted}\n")

    # Sprawdzenie poprawności
    if bubble_sorted == verified_sorted and quick_sorted == verified_sorted:
        print("Obie metody sortowania dają poprawne wyniki.")
    else:
        print("Wyniki sortowania są niezgodne z oczekiwanym rezultatem.")