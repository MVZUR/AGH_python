import multiprocessing
import random
import time
import matplotlib.pyplot as plt

# Funkcja do równoległego sortowania
def merge_sort_parallel(data, pool):
    """Sortuje listę równolegle z wykorzystaniem algorytmu merge sort i multiprocessing."""
    if len(data) <= 1:
        return data

    # Podziel dane na dwie części
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Równolegle sortuj lewą i prawą część
    sorted_sublists = pool.map(merge_sort, [left, right])

    # Scal posortowane części
    return merge(sorted_sublists[0], sorted_sublists[1])

def merge_sort(data):
    """Rekurencyjne sortowanie (używane przez procesy potomne)."""
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    # Sortowanie bez równoległości w procesie potomnym
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    """Scal dwie posortowane listy."""
    result = []
    i = j = 0

    # Dopóki obie listy mają elementy, wybierz najmniejszy
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Dodaj pozostałe elementy z lewej i prawej listy
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Funkcja do testowania
def test_merge_sort_parallel():
    sizes = [100, 1000, 10000, 50000, 100000]
    num_processes = [1, 2, 4, 8, 16]
    results = []

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        for processes in num_processes:
            with multiprocessing.Pool(processes) as pool:
                start_time = time.time()
                merge_sort_parallel(data, pool)
                end_time = time.time()
                results.append((size, processes, end_time - start_time))
    return results

# Główna część programu
if __name__ == '__main__':
    results = test_merge_sort_parallel()

    # Wizualizacja wyników
    plt.figure(figsize=(12, 6))
    for processes in sorted(set(result[1] for result in results)):
        x = [result[0] for result in results if result[1] == processes]
        y = [result[2] for result in results if result[1] == processes]
        plt.plot(x, y, marker="o", label=f"{processes} procesy")

    plt.title("Czas sortowania merge sort równoległego dla różnych rozmiarów i liczby procesów")
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (s)")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend(title="Liczba procesów")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
