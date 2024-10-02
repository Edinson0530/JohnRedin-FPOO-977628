def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Aplicar inserción directa en los subarreglos
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Ejemplo de uso
arr = [3, 5, 4, 10, 6, 9, 7, 1, 2, 8]
print("Arreglo original:", arr)
shell_sort(arr)
print("Arreglo ordenado:", arr)
