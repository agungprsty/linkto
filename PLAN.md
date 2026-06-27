# Project Plan: Link-in-Bio SaaS Platform: linkto.com

## 1. Executive Summary

Proyek ini bertujuan untuk membangun platform *Link-in-Bio Software as a Service* (SaaS) yang memungkinkan pengguna (kreator, UMKM, dan *affiliator*) membuat satu halaman pendaratan khusus untuk mengonsolidasikan semua tautan penting mereka. Fokus utama proyek ini adalah performa tinggi (*fast loading*), stabilitas, arsitektur *mobile-first*, serta skalabilitas dalam menangani *traffic spike*. Sebagai nilai tambah (*value-add*), platform akan menyediakan komponen khusus berupa etalase tautan afiliasi.

## 2. Arsitektur Sistem & Tech Stack

Sistem dirancang dengan pendekatan *decoupled architecture* (pemisahan *backend* dan *frontend*) untuk memastikan performa yang cepat dan siklus iterasi fitur yang mulus.

* **Backend (REST API):** FastAPI (Python). Dipilih karena performa asinkronnya yang sangat cepat (menggunakan ASGI), validasi data otomatis menggunakan Pydantic, dan sangat kompatibel dengan arsitektur data NoSQL. Driver yang disarankan: `Motor` (Asynchronous Python driver for MongoDB) atau ODM seperti `Beanie`.
* **Frontend (Public Page & Dashboard):** Nuxt.js (Vue.js). Dipilih karena kemampuan *Server-Side Rendering* (SSR) yang krusial untuk SEO halaman *public bio*, serta ekosistem Vue yang solid untuk membuat *dashboard interaktif* (seperti manipulasi *drag-and-drop*).
* **Database Utama:** MongoDB (NoSQL). Menawarkan skema dokumen yang fleksibel (JSON-like), sangat cocok untuk menyimpan metadata tautan yang tipe dan formatnya bisa berubah-ubah tanpa perlu migrasi skema yang rumit.
* **Caching & Session (Opsional/Fase Lanjut):** Redis. Digunakan untuk menyimpan sementara data profil pengguna dan antrean (*queue*) pencatatan analitik saat trafik memuncak.
* **Deployment & Containerization:** Docker. Memastikan konsistensi *environment* dari tahap *development* hingga *production*.

## 3. Peta Jalan Fitur (Minimum Viable Product - MVP)

### Phase 1: Core System & Authentication

* Koneksi asinkron FastAPI ke MongoDB.
* Registrasi dan Login pengguna (Email/Password & OAuth Google).
* Manajemen sesi dan otorisasi JWT (JSON Web Token).
* Pembuatan *username* unik (*slug* untuk URL).

### Phase 2: Link Management (Dashboard)

* Antarmuka *dashboard* menggunakan Vue/Nuxt.
* CRUD (Create, Read, Update, Delete) untuk tautan.
* Pengaturan urutan tautan menggunakan mekanisme *drag-and-drop* (mengubah nilai `sort_order`).
* Dukungan *multiple link types*: `standard` (tombol biasa) dan `affiliate_product` (kartu gambar produk).

### Phase 3: Public Bio Page (User Facing)

* Halaman pendaratan publik dengan URL dinamis (contoh: `[domain.com/username](https://domain.com/username)`).
* Desain responsif yang memprioritaskan antarmuka *mobile*.
* Opsi kustomisasi tema dasar (warna latar belakang, gaya tombol).


### Phase 4: Tracking & Analytics (Time-Series Data)

* Pencatatan *event* asinkron untuk setiap kunjungan halaman (*page views*) dan klik tautan (*link clicks*).
* *Dashboard* analitik sederhana yang menampilkan metrik pertumbuhan pengunjung.

## 4. Skema Database (MongoDB Document Design)

Karena menggunakan NoSQL, kita memanfaatkan desain dokumen JSON/BSON. Tautan (*links*) dapat dipisahkan menjadi *collection* tersendiri agar tidak mencapai batas ukuran dokumen jika jumlahnya masif, atau di-*embed* langsung di dalam `users` jika diasumsikan jumlah tautan selalu di bawah batas wajar. Untuk kemudahan analitik dan pembaruan, pemisahan *collection* (*Referencing*) lebih disarankan.

**Collection: `users**`

```json
{
  "_id": ObjectId("..."),
  "username": "agung_dev",
  "email": "user@example.com",
  "password_hash": "hashed_string",
  "profile": {
    "full_name": "Agung Prasetyo",
    "bio": "Backend Software Engineer | Tech Enthusiast",
    "avatar_url": "https://storage.com/avatar.jpg"
  },
  "tier": "free", // 'free', 'pro', 'business'
  "created_at": ISODate("2026-06-28T12:10:45Z"),
  "updated_at": ISODate("2026-06-28T12:10:45Z")
}

```

**Collection: `links**`
*Struktur dinamis yang bisa diubah tergantung pada `type` tautan tersebut.*

```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."), // Referensi ke pengguna
  "title": "Portofolio Github",
  "url": "https://github.com/...",
  "type": "standard", // 'standard' atau 'affiliate_product'
  "image_url": null, // Diisi jika tipe adalah affiliate
  "sort_order": 1,
  "is_active": true,
  "created_at": ISODate("2026-06-28T12:10:45Z")
}

```

**Collection: `analytics**`
*Dioptimalkan sebagai Time-Series Collection di MongoDB untuk performa baca/tulis data agregasi trafik yang masif.*

```json
{
  "_id": ObjectId("..."),
  "user_id": ObjectId("..."),
  "link_id": ObjectId("..."), // null jika ini adalah kunjungan profil (page view)
  "event_type": "link_click", // 'page_view' atau 'link_click'
  "metadata": {
    "referrer": "instagram.com",
    "device": "mobile",
    "geo_location": "Yogyakarta"
  },
  "timestamp": ISODate("2026-06-28T12:10:45Z")
}

```

## 5. Kontrak API (API Design Standard)

Pendekatan *endpoint* memisahkan akses publik (*read-only*) dan akses *dashboard* (*protected*).

**Public Endpoints (No Auth required):**

* `GET /api/v1/bio/{username}` -> Menarik data profil *user* dan daftar tautan aktif (dioptimalkan dengan Redis).
* `POST /api/v1/track/view` -> Mencatat kunjungan halaman.
* `POST /api/v1/track/click` -> Mencatat klik tautan.

**Protected Endpoints (JWT Auth required):**

* `GET /api/v1/user/profile` -> Mengambil data *user* yang sedang *login*.
* `PUT /api/v1/user/profile` -> Memperbarui *bio*, *avatar*, atau tema.
* `GET /api/v1/links` -> Mengambil semua tautan milik *user*.
* `POST /api/v1/links` -> Menambah tautan baru.
* `PUT /api/v1/links/{id}` -> Memperbarui tautan atau `sort_order`.
* `DELETE /api/v1/links/{id}` -> Menghapus tautan.
* `GET /api/v1/analytics/summary` -> Menarik rekap data klik dan penayangan untuk *dashboard*.

## 6. Strategi Eksekusi & Manajemen Proyek

Sebagai standar pengembangan agar proyek berjalan sistematis:

1. **Environment Setup:** Inisialisasi repositori Git dan konfigurasi *Docker-compose* untuk menjalankan MongoDB, Redis, dan server lokal dalam satu perintah.
2. **API First Development:** Membangun dan menguji seluruh logika *backend* menggunakan *tools* seperti Postman/Swagger sebelum menyentuh antarmuka UI.
3. **Frontend Integration (Nuxt.js):** Menghubungkan Nuxt.js dengan *endpoints* API yang sudah matang, dimulai dari *dashboard management* kemudian *public page*.
4. **Performance Tuning:** Mengaktifkan mekanisme *caching* Redis untuk `GET /api/v1/bio/{username}` dan memastikan sistem tidak tumbang saat simulasi beban lalu lintas (*load testing*).

## 7. Model Bisnis & Ekspansi Jangka Panjang

* **Fase 1 (Growth & User Acquisition):** Menyediakan layanan secara gratis 100% untuk membangun basis pengguna. Halaman publik pengguna bertindak sebagai medium pemasaran organik (efek *flywheel*).
* **Fase 2 (Monetization):** Meluncurkan paket berlangganan "Pro" yang membuka fitur analitik terperinci (integrasi *Pixel Tracker* Meta/TikTok), penghapusan *watermark* platform, dan kustomisasi domain mandiri (*Custom Domain*).