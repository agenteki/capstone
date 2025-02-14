**Capstone Cendekia Putra Perdana**
**JCDS 2602**
**BSD CAMPUS**


# Capstone Project 1: 
# Aplikasi gudang produk menscare

## Penjelasan Aplikasi

Aplikasi gudang dalam produk retail merupakan elemen krusial yang menghubungkan jalur produksi hingga penjualan. Sistem manajemen gudang yang efektif tidak hanya membantu dalam pencatatan stok, tetapi juga meningkatkan efisiensi operasional, mengurangi risiko kehabisan atau kelebihan stok, serta mempercepat proses distribusi.

Dalam industri produk sabun yang memiliki berbagai varian, ukuran, dan kemasan, manajemen stok yang baik sangat diperlukan untuk menghindari ketidakseimbangan persediaan yang dapat berdampak pada efisiensi bisnis. Dengan sistem pencatatan yang akurat, perusahaan dapat mengontrol jumlah bahan baku seperti minyak esensial, bahan aktif, dan kemasan, sehingga produksi dapat berjalan sesuai permintaan pasar tanpa pemborosan.

Dalam era digital dan persaingan bisnis yang semakin ketat, penggunaan aplikasi gudang dalam produk retail bukan lagi pilihan, tetapi menjadi kebutuhan utama untuk menjaga daya saing dan memastikan operasional bisnis berjalan dengan lancar.


## Analisis Mengapa Aplikasi Gudang Dibutuhkan

**1.Mengurangi Human Error**
1. Kesalahan pencatatan stok secara manual dapat menyebabkan ketidaksesuaian antara stok fisik dan data.
2. Human error dalam input data dapat berdampak pada kelebihan atau kekurangan stok, yang akhirnya mempengaruhi produksi dan penjualan.

**2.Efisiensi Operasional**
1. Aplikasi gudang memungkinkan pencatatan barang masuk dan keluar secara otomatis, mengurangi keterlambatan dalam proses inventarisasi.
2. Mengoptimalkan tata letak gudang agar pengambilan barang lebih cepat dan terorganisir.
Meminimalkan Risiko Kehabisan atau Kelebihan Stok.

**3.Keamanan Data dan Aksesibilitas**
1. Data stok tersimpan dalam sistem yang aman dan dapat diakses oleh pihak berkepentingan dengan hak akses tertentu.
2. Aplikasi gudang mempercepat proses inventarisasi, pemesanan ulang, dan analisis stok, sehingga perusahaan dapat mengalokasikan sumber daya untuk hal yang lebih strategis.

## Aplikasi Gudang dalam Capstone Modul 1

Dalam Capstone Modul 1, saya telah membuat aplikasi sederhana yang mencakup fungsi CRUD (Create, Read, Update, Delete) untuk mengelola data inventory.

Fungsi ini memungkinkan pengguna untuk menambahkan data baru, melihat informasi stok, memperbarui data produk, dan menghapus item yang tidak diperlukan. Dengan fitur ini, pencatatan inventory menjadi lebih efisien, mengurangi kesalahan, dan mempercepat proses pengelolaan stok.

Meskipun sederhana, aplikasi ini menjadi langkah awal dalam memahami sistem manajemen data dan dapat dikembangkan lebih lanjut sesuai kebutuhan.

## Penjelasan Fungsi dalam Aplikasi Gudang Stock Menscare ##

**1. Struktur Data (Dictionary) untuk Stok Gudang**
Variabel `gudang_sabun` → Dictionary berisi data stok produk sabun berdasarkan jenis produk, varian, SKU, ukuran, harga, dan jumlah stok.

**2. Fungsi Tampilan Menu**
`tampilan_menu()` → Menampilkan pilihan menu utama untuk pengguna.

**3. Fungsi Menampilkan Stok**
- `tampilan_stok()` → Menampilkan seluruh stok gudang dalam bentuk tabel.
- `tampilan_stok_berdasarkan_produk(jenis)` → Menampilkan stok berdasarkan jenis produk tertentu.
- `tampilan_stok_berdasarkan_varian(produk, varian)` → Menampilkan stok berdasarkan varian dalam produk tertentu.

**4. Fungsi Menambahkan Produk atau Varian Baru**
`masukan_produk()`
- Menampilkan stok saat ini.
- Memungkinkan pengguna menambahkan produk baru jika belum ada.
- Menambahkan varian baru ke dalam produk yang ada.
- Memasukkan SKU baru dan memvalidasi input untuk ukuran, harga, dan stok.

**5. Fungsi Memperbarui Stok dan Harga SKU**
`perbarui_stok_harga()`
- Menampilkan stok saat ini.
- Memvalidasi input jenis produk dan varian yang ingin diperbarui.
- Memeriksa keberadaan SKU dan meminta input harga dan stok baru dengan validasi error handling (try-except).
- Memperbarui harga dan stok pada SKU yang dipilih.

**6. Fungsi Menghapus Produk, Varian, atau SKU**
`hapus_produk()`
- Memeriksa apakah pengguna adalah admin (memerlukan password).
- Memungkinkan penghapusan seluruh jenis produk, varian tertentu, atau SKU tertentu.
- Jika hanya SKU tertentu yang dihapus, daftar varian diperbarui tanpa SKU yang dihapus.

**7. Keamanan dan Validasi Input**
- Menggunakan try-except untuk menangani input yang tidak valid (misalnya angka negatif atau karakter non-numerik dalam harga/stok).
- Memastikan admin memiliki akses terbatas untuk menghapus data dengan validasi password.

