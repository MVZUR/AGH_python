import multiprocessing

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

# Główna funkcja
if __name__ == "__main__":
    import random

    # Generowanie losowej listy
    data = [random.randint(0, 100) for _ in range(20)]
    print("Nieposortowane dane:", data)

    # Tworzenie puli procesów
    with multiprocessing.Pool() as pool:
        sorted_data = merge_sort_parallel(data, pool)

    print("Posortowane dane:", sorted_data)
