# TUGAS 3

### Q3.1
**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.** <br>
Ketiga fungsi ini akan dibuat di dalam aplikasi `main` yang sudah dibuat sebelumnya. 
<br>
Sebagai sebuah basis sebelum kita menghubungkan aplikasi dengan database (model Item) <br>

1. register: <br>
	- Dalam `views.py` import <br>
	`UserCreationForm` dari `django.contrib.auth.forms` <br>
	`redirect` dari `django.shortcuts` <br>
	`messages` dari `django.contrib` <br>
	- buatlah fungsi baru bernama `register` yang mengambil `request` <br>
	- Kita menggunakan sebuah user creation form untuk membuat user baru di web app kita, jika info register sudah valid maka kita akan membuat user baru dengan `form.save()` dan redirect user ke login page <br>
	- Buat sebuah template bernama `register.html` di dalam folder `templates` di `main` <br>
	- Buatlah sebuah form dengan method `POST` yang akan mengirimkan data ke `register` view function <br>
	- Dalam `urls.py` di `main` tambahkanlah sebuah routing baru untuk halaman register <br>
2. Login: <br>
	- Dalam `views.py` import `authenticate` dan `login` dari `django.contrib.auth` <br>
	- Buatlah sebuah function baru bernama `login` yang mengambil `request`, dalam function ini, kita menggunakan POST untuk mengembalikan detail login (username dan password) dan mengautentikasi dengan `authenticate()` jika valid, kita redirect user ke main page, dan jika tidak kita akan mengirim message error <br>
	- Buatlah sebuah template bernama `login.html` di dalam folder `templates` di `main` <br>
	- Buatlah sebuah form dengan method `POST` yang akan mengirimkan data ke `login` view function, di bawah form kita akan juga anchor link ke regitster page jika user belum mempunyai user account  <br>
	- Dalam `urls.py` di `main` tambahkanlah sebuah routing baru untuk halaman login <br>
3. Logout: <br>
	- Dalam `views.py` import `logout` dari `django.contrib.auth` <br>
	- Buatlah sebuah function baru bernama `logout` yang mengambil `request`, dalam function ini, kita menggunakan function `logout(request)` dan return sebuah `redirect` ke login page <br>
	- Dalam main page, kita akan menambahkan sebuah button yang akan mengarahkan user ke logout page <br>
	- Dalam `urls.py` di `main` tambahkanlah sebuah routing baru untuk halaman logout <br>

Kita akan menambahkan restriksi login untuk fungsi dasar di web app kita, sehingga user tidak bisa mengakses page lain jika belum login. <br>
- Dalam `views.py` import `login_required` dari `django.contrib.auth.decorators` <br>
- Tambahkan decorator `@login_required` di setiap view function yang ingin kita restriksi (show_main)<br>


### Q3.2
**Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**

---

# TUGAS 2

### Q2.1
 **Membuat input `form` untuk menambahkan objek model pada app sebelumnya.** <br>
- Dalam Virtual enviroment yang active, kita perlu membuat sebuah *Skeleton* yang menjadi basis dari HTML kita, ini dilakukan agar semua aplikasi mempunyai tampilan yang konsisten di *views* <br>
- Pada *root* directory buatlah sebuah folder templates dan isi dengan file `base.html`, yang akan menjadi "base" dari HTML yang akan dibuat dari sekarang <br>
- Pada file `settings.py` dalam direktori projek `player_inventory`, kita akan menambah template yang ada di dalam *root* directory, dengan menambah `BASE_DIR/'templates'`, kepada `TEMPLATES` <br>
- Pada file `main.html` dalam aplikasi `main` , konfigurasilah agar meng-extend dari template dasar `base.html` dengan menggunakan `{%extends 'base.html' %}` dna mendeklarasi block yang akan dipakai <br> <br>

- Model `item` saya merupakan sebuah class dengan 3 attribut, form perlu mengisi 3 atribut tersebut, karena ini `fields` yang perlu diisi dari form adalah name, amount, dan description <br>
- pada direktori `main` buatlah sebuah file bernama `forms.py`, yang merupakan code dari form yang akan dibuat buatlah sebuah class form `itemform` dengan meta class denagn atribut `fields` yang merupakan sebuah list yang terisi dengan atribut yang ingin dimasukkan sebagai input <br>
- Import beberapa library (termasuk form class yang baru dibuat) kepada `views.py`:
	1. `HttpResponseRedirect`, yang merupakan subclass dari `HttpResponse`, yang berguna untuk meredirect user kepada url spesifik <br>
	2. `reverse` yang membantu kita untuk tidak hardcode url full dan memakai *url pattern*<br>
-  Dalam `views.py` ini saya membuat function bernama `create_item` yang mengambil `request.post` dan membuat ItemForm baru berdasarkan request.post user, mengvalidasi input form (`form.is_valid`), save form (`form.save`) dan redirect user ke main page setelah selesai. <br>
- dalam file urls.py di main kita akan tambahkan routing baru untuk halaman form yang kita sudah buat <br>
- Setelah route telah dibuat, kita membuat tampilan dari form yang akan menjadi tempat menginput attribut. Ini dibuat dalam folder `templates` di `main` yang bernama `create_item.html` <br>
-  menggunakan `{{forms.as_table}}` , ini akan merender `fields` yang kita masukkan di fungsi create_item tadi menjadi tempat input untuk attribut-attribut yang kita masukkan. ini akan merender fields yang kita declare tadi sebagai `<tr>` di HTML. <br>
- Buatlah component input dengan tipe submit untuk mengkonfirmasi request ke view dan memassukan info Item ke database <br>
- Untuk mengakses form ini kita membuat sebuah anchor yang berupa button yang akan me-*redirect* ke page create_item <br>

---

### Q2.2
**Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML _by ID_, dan JSON _by ID_** <br>

Dalam `views.py` kita bisa membuat function-function untuk mendisplay info tentang Models yang sudah dibuat dan tersimpan dengan berbagai format: 
- format html: <br>
	dalam fungsi `show_main` kita akan menambah context baru yaitu object `items` yang dideclare dengan menggunakan `Item.objects.all`, ini merupakan kumpulan data object `Item` yang sudah ada di database, dalam html main kita akan mmebuat sebuah tabel yang menunjukkan semua item yang sudah dibuat dengan mengiterasi di sebuah for loop dengan attribut yang sesuai.
- format JSON dan XML (semua `Item`): <br>
	Buat function baru bernama `show_json`/ `show_xml` dan seperti tadi declare sebuah variable data dan *retrieve* semua object Item yang ada menggunakan `Item.objects.all`, sehabis ini kita akan meng-*serialize* data yang ada menggunakan method `serialize` dari module `serializers` dari library `django.core`. <br>
	
	meng-*serialize* data intinya dalah untuk mengubah sebuah struktur data atau *object state* menjadi format yang bisa disimpan, ditransmit, atau dibagi dalam representasi text. <br> 
	Untuk Json, Kita akan mengserialize data meggunakan `serializers.serialize("json",data)` dan return sebuah object Http response dengan content type `application/json` <br>
	Untuk XML, kita mengserialize data dengan menggunakan `serializers.serialize("xml",data)` dan return object Http response dengan content type `application/xml` <br>
	Sebuah content type adalah sebuah header yang mengindikasi tipe media atau format resource yang dikirim atau diterima.
- Format JSON dan XML (1 Item): <br>
	Untuk mengfilter item yang diinginkan kita bisa mengfilter item yang ada di data dengan id unik yang diberikan saat dibuat. ini bisa dilakukan dengan memakai .filter(pk=id) pada manager class Item.
	`Item.objects` merepresentasikan manager untuk model `Item` dan memungkinkan kita untuk melakukan query yang ingin dilakukan pada tabel Item di database <br>
	`.filter(pk=id)` digunakan untuk mengfilter query berdasarkan pk/primary key, dalam kasus ini adalah `id`, dan akan mereturn queryset yang cocok.
	metode untuk mereturn sama saja seperti format JSON dan XML biasa.


### Q2.3

---

**Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.** <br>
Dalam `urls.py` di main kita akan routing semua function Http request yang kita sudah buat ke urlnya sendiri (dibawah `main/`) <br>
langkah pertama pastinya adalah untuk mengimport function-function yang sudah kita buat dengan <br>
	`from main.views import show_json, show_xml, show_xml_by_id, show_json_by_id`
, di list urlpatterns, dengan menggunakan `path`, kita akan routing url yang berbeda untuk semua function yang sudah dibuat. <br>
untuk format JSON dan XML: <br>
	`path('json/', show_json, name='show_json'), path('xml/', show_xml, name='show_xml')` <br>
untuk JSON dan XML dengan id: <br>
	`path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'), path('json/<int:id>', show_json_by_id, name='show_json_by_id')`


### Q2.4

---

**Apa perbedaan antara form `POST` dan form `GET` dalam Django?** <br>
Dalam Django, `POST` dan `GET` merupakan hanya kedua Http request yang dipakai saat menggunakan forms. <br>
Saat menggunakan `GET` , semua data form di encode ke dalam url dan diaapend ke url sebagai parameter query,URL berisi alamat tujuan pengiriman data, serta kunci dan nilai data. Karena ini, GET method dilimit oleh apa yang bisa dimasukkan ke dalam URL, dan yang diperblehkan hanya karakter ASCII. <br>
Saat menggunakan `POST`, data form berada di dalam *message body* dalam Http request. <br>
Dibandingkan dengan `POST`, `GET` kurang secure. <br>
Sebuah request yang bisa mengubah sistem harus menggunakan `POST`

---

### Q2.5
**Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?** <br>

1. **Struktur data**:
	- XML (Extensible Markup Language) menyimpan data dalam struktur pohon dengan namespace untuk kategori data yang berbeda. XML digunakan untuk menyimpan dan mengirim data yang terstruktur dengan tag yang dapat didefinisikan oleh pengguna.
	- JSON (JavaScript Object Notation) menggunakan struktur seperti map dengan key-value pair. JSON digunakan untuk mengirim dan menyimpan data yang terstruktur dengan syntax yang ringkas dan mudah dibaca.
	- HTML (HyperText Markup Language) digunakan untuk membangun web page dan menentukan bagaimana konten akan ditampilkan di browser. HTML menyimpan data dalam struktur bertingkat dengan tag dan atribut yang telah ditentukan sebelumnya.

2. **Efisiensi dan ukuran file**:
	- JSON memiliki ukuran file yang lebih kecil dan transmisi data yang lebih cepat dibandingkan dengan XML karena syntax yang padat
	- XML memiliki struktur tanda yang lebih kompleks untuk ditulis dan dibaca.
	- HTML memiliki ukuran file yang bervariasi tergantung pada kompleksitas web page yang dibangun

3. **Keamanan**:
	- XML dan JSON rentan terhadap serangan keamanan seperti serangan injeksi dan serangan DoS (Denial of Service)
	- XML memiliki risiko keamanan yang lebih tinggi karena mendukung DTD (Document Type Definition) yang dapat digunakan untuk mengeksekusi kode berbahaya
	- JSON lebih aman daripada XML karena tidak memiliki fitur seperti DTD yang rentan terhadap serangan

4. **Penggunaan**:
	- XML digunakan dalam berbagai industri dan aplikasi, seperti natrual language processing, pertukaran data antar sistem, konfigurasi aplikasi, dan penyimpanan data
	- JSON banyak digunakan dalam pengembangan web dan aplikasi mobile karena syntax yang sederhana dan mudah dibaca dan ditulis oleh manusia dan mesin
	- HTML digunakan untuk membangun halaman web dan menentukan tampilan dan struktur konten di browser


---

### Q2.6
**Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?** <br>
Seperti yang disebut di dalam perbedaan-perbedaan tadi , JSON, atau JavaScript Object Notation sangat populer dikarenakan: <br>
- Syntax yang mudah dibaca oleh manusia dan diparse oleh mesin, karena ini tidak memerlukan kode tambahan untuk diproses
- Ukuran filenya yang kecil membantu dalam mempercepat transfer data dan hasil dari web service
- Kebanyakan framework di dunia aplikasi web menggunakan JavaScript sebagai dasarnya, JSON merupakan representasi object dari JavaScript, karena ini JSON merupakan cara paling mudah untuk memanipulasi dan menyimpan data dalam dunia aplikasi web.

---

### Q2.7
**Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**

![HTML](ReadmeImg/HTML.png)

![JSON](ReadmeImg/JSON.png)

![XML](ReadmeImg/XML.png)

![JSON_ID](ReadmeImg/JSONID.png)

![XML_ID](ReadmeImg/XMLID.png)

---

### Q1.1
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**Membuat sebuah proyek Django baru.** <br>
- Membuat directory baru bernama player_inventory dengan menggunakan `django-admin startproject player_inventory .`, membuatnya menjadi sebuah git repository <br>
-  Menghubungkan Git Lokal dengan repository di Github. Dan set branch lokal menjadi main (dalam step ini saya belum push) <br>
- Membuat sebuah virtual enviroment di dalam directory, dengan menggunakan `python - m venv env`, dan mengaktifkanya. <br>
- Menambahkan dependencies yang diperlukan ke dalam virtual envioment, dependencies merupakan komponen atau modul software yang diperlukan saat development. <br>
- Konfigurasi settings.py dalam project agar bisa mendeploy <br>
- Menambah berkas .gitignore, dan membuat supaya hanya file yang diperlukan akan dipush <br>
	

**Membuat aplikasi dengan nama main pada proyek tersebut.** <br>
- Mengaktivasi Virtual enviroment dalam directory utama. <br>
- dalam directory ini, buatlah sebuah app bernama 'main'(dalam sebuah web app, 'app' mempunyai arti spesifik, seperti sebuah home page atau form contact CS), dengan menggunakan `python manage.py startapp main` <br>
- dalam direktori utama project, tambahkan `main` ke dalam list `INSTALLED_APPS`
	yang terletak di dalam settings.py <br>
- dalam direktori `main`, buatlah direktori baru `templates`, dalam direktori ini buatlah html file bernama `main` <br>
	   
**Melakukan routing pada proyek agar dapat menjalankan aplikasi main.** <br>
- Dalam direktori utama, buka file `urls.py`, dan dari `django.urls` import `path`, dan `include` <br>
- untuk menambahkan path `main` ke project tambahlah `path('main/', include('main.urls'))` dalam `urlpatterns` <br>
- ini menambahkan routing `main` ke url project dan akan terlihat saat memasukkan `example.com/main` ke browser <br>


**Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.** <br>
- isi berkas `models.py` dengan models yang akan di migrate. <br>
- dalam kasus tugas, model yang akan dipakai bernama `item`, dimana ia mempunyai atribut `name` yang merupakan CharField, `amount` yang merupakan IntegerField, dan `description` yang merupakan TextField. <br>
- Class ini menginherit dari kelas dasar `models` dari Django, yang mendefinisikan semua atribut dari kelas sebagai kolom di database, ini merupakan bagian dari Object-Relational Mapping (ORM) system Django yang memungkinkan kita untuk menentukan struktur dan perilaku data. <br>
- sehabis membuat model, jalankan perintah `python manage.py makemigrations`, ini menyiapkan query database project untuk memasuki data yang sesuai dengan model yang sudah diberikan <br>
- sehabis itu jalankan `python manage.py migrate`, ini akan mengaplikasikan perubahan model dalam file migrasi <br>


**Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.** <br>
- Dalam direktori `main` buka file `views.py`, dan dari library `django shortcuts` import `render`, ini untuk me-render tampilan HTML dengan data yang diberikan <br>
- Tambahkan fungsi `show_main` dengan paramater request <br>
- isi `context` dengan data yang ingin ditampilkan <br>
- untuk page saya, context merupakan zipped list dari 3 list berbeda `name`, `amount`, dan `description` yang akan di render di `main.html` <br>

**Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.** <br>
- Membuat file `urls.py` dalam direktori main <br>
- import fungsi `path` dari `django.urls` untuk mendefisnisikan URL pattern <br>
- import function `show_main` yang dibuat di views.py <br>
- set `app_name` menjadi `main`, ini menjadi namespace pattern URL app yang dibuat <br>
- mengisi file dengan URL_PATTERN yang mengarah ke function `show_main` yang dibuat dalam `views.py` <br> 
- dengan konfigurasi ini, saat user datang ke url yang disetting, `show_main` view function akan dicall untuk menghandle requst <br>


**Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.** <br>
- membuat sebuah app baru di Adaptable yang terhubung ke github. <br>
- Buat Python App Template sebagai template deployment dan PostgreSQL sebagai tipe basis data dan deploy aplikasi dengan start command `python manage.py migrate && gunicorn player_inventory.wsgi`. <br>


---

### Q1.2
**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
![Database Image](ReadmeImg/Database.png)

Urls.py berfungsi untuk menghubungkan antara url yang diakses oleh user dengan views.py. <br>
Urls.py akan mengarahkan user ke views.py yang akan menentukan apa yang akan ditampilkan ke user. <br>
Views.py akan mengambil data dari models.py yang berisi data yang akan ditampilkan ke user. <br>
Setelah itu, views.py akan mengirimkan data ke html yang akan ditampilkan ke user.

---

### Q1.3
**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?** <br>
    
- kita menggunakan virtual enviroment untuk membuat sebuah lingkungan yang 'terisolasi' dimana kita bisa menginstall dependencies dan versi framework yang kita inginkan tanpa adanya dampak secara global di mesin kita, ini berguna jika misalnya kita memperlukan suatu versi python atau django yang spesifik untuk suatu project yang kita ingin kerjakan, dengan virtual enviroment, 'lingkungan' ini akan bisa dikerjakan dengan versi yang diperlukan dan kita bisa activate dan deactivate saat kita selesai mengerjakanya. Kita tetap bisa membuat sebuah aplikasi web django tanpa menggunakan virtual enviroment, namun ini tidak direkomendasikan, karena misalnya jika kita ingin mengerjakan project yang berbeda tanpa menggunakan virtual enviroment, dependecies akan terinstall secara global, hal ini bisa berdampak buruk jika kita ingin mengerjakan suatu project baru dengan dependencies dan versi django yang berbeda.

---

### Q1.4
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- **MVC**
    Model-View-Controller (MVC) merupakan pola arsitektur aplikasi yang memisahkan code menjadi:<br>
        Model -> Bagian logika data aplikasi yang akan didisplay atau dimanipulasi <br><br>
        View -> Bagian yang menampilkan informasi dengan bentuk UI<br><br>
        Controller -> Bagian "logika" aplikasi yang mengubungkan model dan view 
        dan mengatur request yang masuk<br>
        
- **MVT**
    Model-Views-Template merupakan pola arsitektur aplikasi yang digunakan oleh Django web framework, implementasinya pada dasarnya sangat mirip dengan MVT, dengan beberapa penamaan yang beda. Salah satu perbedaan yang utama adalah di MVT Controller sudah ada dari framework dan tidak perlu dicode sendiri.<br>
        Model -> Dalam Django model sama saja dengan bagian model di MVC, yaitu sebuah logika data aplikasi yang biasanya direpresentasikan oleh database yang didisplay atau dimanipulasi. <br> <br>
        View -> Dalam Django, view lebih menyerupai "Controller" arsitektur MVC, dimana ia menyerupai handler untuk memproses http request dan mengembalikan response menggunakan data dari `model` dan merender UI dari `Template`<br><br>
        Template -> Dalam Django, Template merupakan struktur atau layout dari UI.<br>

- **MVVM**
    Model-view-viewmodel merupakan pola arsitektur yang memisah pengembangan GUI (View) dan logika bisnis (model), ini dilakukan agar 'view' tidak bergantung pada skema 'model' yang spesifik <br>
        Model -> Merupakan model yang merepresentasikan data yang digunakan pada logika bisnis <br> <br>
        View -> Merupakan struktur UI yang juga menerima user input <br> <br>
        ViewModel -> Terletak di antara model dan View, ViewModel mempunyai controls untuk berinteraksi dengan view, berbeda dengan MVC, MVVM mempunyai sebuah *Binder* yang berkomunikasi dengan view dan properti di viewmodel. <br> 

---