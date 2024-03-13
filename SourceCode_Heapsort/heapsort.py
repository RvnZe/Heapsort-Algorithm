def tumpuk(arr, n, i):
    terbesar = i
    kiri = 2 * i + 1
    kanan = 2 * i + 2
    
    # Periksa apakah anak kiri lebih besar daripada root
    if kiri < n and arr[kiri] > arr[terbesar]:
        terbesar = kiri
    
    # Periksa apakah anak kanan lebih besar daripada root atau anak kiri
    if kanan < n and arr[kanan] > arr[terbesar]:
        terbesar = kanan
    
    # Jika terbesar bukan root
    if terbesar != i:
        arr[i], arr[terbesar] = arr[terbesar], arr[i]
        
        # Rekursif tumpuk pada sub-pohon yang terpengaruh
        tumpuk(arr, n, terbesar)

def heapsort(arr):
    n = len(arr)
    
    # Bangun heap awal
    for i in range(n//2 - 1, -1, -1):
        tumpuk(arr, n, i)
    
    # Ekstraksi elemen satu per satu dari heap
    for i in range(n-1, 0, -1):
        # Tukar elemen teratas dengan elemen terakhir
        arr[0], arr[i] = arr[i], arr[0]
        
        # Panggil tumpuk untuk membangun heap pada bagian yang tersisa
        tumpuk(arr, i, 0)

# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Array yang diurutkan:")
print(arr)
