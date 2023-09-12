https://best-inventory-app.adaptable.app/

### Q1
**Membuat sebuah proyek Django baru.**
	- Membuat directory baru bernama player_inventory dengan menggunakan `django-admin startproject player_inventory .`, membuatnya menjadi sebuah git repository 
	-  Menghubungkan Git Lokal dengan repository di Github. Dan set branch lokal menjadi main (dalam step ini saya belum push)
	- Membuat sebuah virtual enviroment di dalam directory, dengan menggunakan `python - m venv env`, dan mengaktifkanya.
	- Menambahkan dependencies yang diperlukan ke dalam virtual envioment, dependencies merupakan komponen atau modul software yang diperlukan saat development.
	- Konfigurasi settings.py dalam project agar bisa mendeploy
	- Menambah berkas .gitignore, dan membuat supaya hanya file yang diperlukan akan dipush
	

**Membuat aplikasi dengan nama main pada proyek tersebut.**
	- Mengaktivasi Virtual enviroment dalam directory utama.
	- dalam directory ini, buatlah sebuah app bernama 'main'(dalam sebuah web app, 'app' mempunyai arti spesifik, seperti sebuah home page atau form contact CS), dengan menggunakan `python manage.py startapp main`
	- dalam direktori utama project, tambahkan `main` ke dalam list `INSTALLED_APPS`
	   yang terletak di dalam settings.py
	- dalam direktori `main`, buatlah direktori baru `templates`, dalam direktori ini buatlah html file bernama `main`
	   
**Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
	- Dalam direktori utama, buka file `urls.py`, dan dari `django.urls` import `path`, dan `include`
	- untuk menambahkan path `main` ke project tambahlah `path('main/', include('main.urls'))` dalam `urlpatterns`
	- ini menambahkan routing `main` ke url project dan akan terlihat saat memasukkan `example.com/main` ke browser


**Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.**
	- isi berkas `models.py` dengan models yang akan di migrate. 
	- dalam kasus tugas, model yang akan dipakai bernama `item`, dimana ia mempunyai atribut `name` yang merupakan CharField, `amount` yang merupakan IntegerField, dan `description` yang merupakan TextField.
	- Class ini menginherit dari kelas dasar `models` dari Django, yang mendefinisikan semua atribut dari kelas sebagai kolom di database, ini merupakan bagian dari Object-Relational Mapping (ORM) system Django yang memungkinkan kita untuk menentukan struktur dan perilaku data.
	- sehabis membuat model, jalankan perintah `python manage.py makemigrations`, ini menyiapkan query database project untuk memasuki data yang sesuai dengan model yang sudah diberikan
	- sehabis itu jalankan `python manage.py migrate`, ini akan mengaplikasikan perubahan model dalam file migrasi


**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
	- Dalam direktori `main` buka file `views.py`, dan dari library `django.shortcuts` import `render`, ini untuk me-render tampilan HTML dengan data yang diberikan
	- Tambahkan fungsi `show_main` dengan paramater request
	- isi `context` dengan data yang ingin ditampilkan
	- untuk page saya, context merupakan zipped list dari 3 list berbeda `name`, `amount`, dan `description` yang akan di render di `main.html`

**Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
	- Membuat file `urls.py` dalam direktori main
	- import fungsi `path` dari `django.urls` untuk mendefisnisikan URL patter
	- import function `show_main` yang dibuat di views.py
	- set `app_name` menjadi `main`, ini menjadi namespace pattern URL app yang dibuat
	- mengisi file dengan URL_PATTERN yang mengarah ke function `show_main` yang dibuat  dalam `views.py` 
	- dengan konfigurasi ini, saat user datang ke url yang disetting, `show_main` view function akan dicall untuk menghandle requst 


**Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
	- membuat sebuah app baru di Adaptable yang terhubung ke github.
	- Buat Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data dan deploy aplikasi dengan start command `python manage.py migrate && gunicorn player_inventory.wsgi`. 


---

### Q2

### Q3
