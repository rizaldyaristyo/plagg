import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')  # Download necessary tokenizer data (only required once)

def calculate_text_similarity(text1, text2):
    # Determine the longer and shorter texts
    if len(text1) > len(text2):
        longer_text = text1
        shorter_text = text2
    else:
        longer_text = text2
        shorter_text = text1

    # Tokenize the texts
    tokens = nltk.word_tokenize(longer_text + ' ' + shorter_text)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Compute TF-IDF features for the longer text
    tfidf_features_longer = vectorizer.fit_transform([longer_text])

    # Transform the shorter text using the same vectorizer
    tfidf_features_shorter = vectorizer.transform([shorter_text])

    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(tfidf_features_longer, tfidf_features_shorter)

    # Extract significant features
    feature_names = vectorizer.vocabulary_
    feature_weights = tfidf_features_longer.toarray()[0]
    significant_features = [(feature, feature_weights[feature_names[feature]]) for feature in feature_names]

    return similarity_matrix[0][0], significant_features

# Example usage:
text1 = r"Dengan pertumbuhan penggunaan smartphone yang terus meningkat dan popularitas yang kian meluas pada smartphone berbasis sistem operasi Android, ancaman keamanan yang ditimbulkan oleh malware dan virus menjadi perhatian yang sangat signifikan. Oleh karena itu, penelitian ini bertujuan untuk menganalisis tingkat efektivitas algoritma Random Forest dalam melakukan klasifikasi aplikasi-aplikasi yang terinfeksi malware. Dataset yang digunakan dalam penelitian ini dibagi menggunakan teknik validasi pembagian 80:20, dengan 80% data digunakan untuk pelatihan dan 20% data untuk pengujian. Hasil penelitian menunjukkan tingkat akurasi yang sangat tinggi, dengan akurasi keseluruhan mencapai 99,14%. Skor presisi dan recall juga menunjukkan performa yang sangat tinggi, dengan masing-masing mencapai 99,07% dan 98,51%. Selain itu, nilai F-score, yang merupakan ukuran kombinasi presisi dan recall, menunjukkan hasil yang sangat baik, yakni 98,79%. Tingkat kesalahan positif (false positive rate) yang terjadi pada model klasifikasi ini sangat rendah, hanya sebesar 0,52%, hal ini menandakan bahwa model mampu mengidentifikasi aplikasi-aplikasi non-malware dengan sangat akurat. Selanjutnya, tingkat kesalahan negatif (true negative rate) pada model ini mencapai 99,48%, yang menandakan kemampuan model dalam mengklasifikasikan aplikasi-aplikasi yang mengandung malware secara tepat. Dalam penelitian ini, GridSearchCV Hyperparameter Optimization digunakan untuk menemukan kombinasi terbaik dari hyperparameter algoritma Random Forest. Dengan demikian, dapat disimpulkan bahwa algoritma Random Forest yang dioptimasi dengan GridSearchCV terbukti sangat efektif dalam mengklasifikasikan aplikasi-aplikasi malware pada smartphone berbasis Android. Temuan ini memiliki implikasi yang sangat penting dalam meningkatkan keamanan smartphone di masa depan."
text2 = r"PDF PROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdf  Winda Ariestya  Academiaedu Academiaedu no longer supports Internet ExplorerTo browse Academiaedu and the wider internet faster and more securely please take a few seconds to upgrade your browser CloseLog InLog in with FacebookLog in with GoogleorEmailPasswordRemember me on this computeror reset passwordEnter the email address you signed up with and well email you a reset link Need an account Click here to sign up Log InSign UpLog InSign UpmoreJob BoardAboutPressBlogPeoplePapersTermsPrivacyCopyrightWere HiringHelp Centerless Download Free PDFDownload Free PDFPROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdfPROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdfPROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdfPROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdfPROCEEDINGS KNSI 2014 ABSTRACT EDITIONpdfWinda AriestyaAbstrak Mendapatkan jawaban terhadap suatu permasalahan yang spesifik sulit dilakukan secara cepat dan murah Misalnya mencari jawaban terhadap permasalahan akuntansi di satu perusahaan yang harus diselesaikan secara cepat Untuk mendapatkannya pihak perusahaan akan mencari disuatu lingkungan khusus konsultan akuntansi Dengan cara seperti itu waktu dan biaya yang digunakan akan sangat banyak sekali Dewasa ini untuk mencari jawaban dengan cepat dan murah sudah bukan lagi sesuatu yang mustahil caranya dapat dilakukan secara instan dengan memanfaatkan teknologi Text Mining dan Big Data dari sebuah komunitas khusus di internet Internet diasumsikan sebagai tempat penyimpanan berbagai macam pengetahuan Untuk mendapatkan pengetahuan di lingkungan khusus akuntansi gunakan media sosial forum akuntansi di internet sementara untuk mendapatkan kualitas jawaban yang baik dilakukan proses perhitungan dengan menggunakan VSM dimana hasilnya merupakan sejumlah jawaban dengan bobotSee Full PDFDownload PDFSee Full PDFDownload PDFRelated PapersPENERAPAN FUZZY LOGIC PADA SISTEM PENDUKUNG PENENTUAN LOYAL CUSTOMERBernadus Very Christioko Dian Tri WiyantiSaat sebuah perusahaan semakin berjaya dalam eksistensinya di masyarakat maka perusahaan tersebut lebih berorientasi untuk memperoleh pelanggan baru Sehingga dimungkinkan suatu saat akan mengakibatkan kehilangan pelanggan jika tidak dimaintain dengan baik Dalam hal ini terdapat variabel kepuasan pelanggan yang mempengaruhi loyalitas pelanggan pada sebuah perusahaan Untuk menjaga hal tersebut maka dalam makalah ini diterapkan penerapan metode logika fuzzy untuk memilih pelanggan yang paling loyal Seberapa loyal seorang pelanggan terhadap suatu perusahaan tentunya tidak bisa dideklarasikan secara pasti atau eksak Sehingga pengambilan keputusannya sangat cocok apabila menggunakan konsep fuzzy karena dapat merepresentasikan variabel yang bersifat samar atau tidak eksak Studi kasus pada penelitian ini dilakukan khususnya pada perusahaan dagang atau swalayan Hasil penerapannya adalah sistem bisa menentukan pelanggan yang paling loyal dari beberapa sampel pelanggan terpilihDownload Free PDFView PDFAPLIKASI SIMPLE ADDITIVE WEIGHTING SAW DALAM PENENTUAN THE MOST LOYAL CUSTOMERDian Tri WiyantiPerdagangan adalah hubungan yang menguntungkan antara kedua belah pihak yaitu pembeli dan penjual Fakta yang ada di lapangan menyebutkan bahwa perusahaan lebih berorientasi untuk memperoleh pelanggan baru namun tidak berfokus pada kehilangan pelanggan loss of customer Padahal variabel kepuasan pelanggan sangat berpengaruh positif dan signifikan terhadap loyalitas pelanggan Dan tentunya berpengaruh juga terhadap eksistensi perusahaan itu sendiri Oleh karena itu perusahaan sebaiknyan menjaga pelanggan yang ada dengan memberikan penghargaan seperti pemilihan the most loyal customer Dalam makalah ini dibuat sistem aplikasi untuk menentukan loyalitas pelanggan menggunakan metode Simple Additive Weighting SAW Dalam metode ini ada 4 kriteria yang digunakan yaitu total belanja keaktifan pelanggan kuantitas datang laba perusahaan per 1 nota belanja pelanggan value increase perusahaan dalam 2 tahun Studi kasus dari sistem ini dilakukan pada salah satu perusahaan dagang atau swalayan Hasil penerapan dari sistem ini adalah sistem yang bisa menentukan siapa pelanggan paling loyal dari sekian sampel pelanggan yang terpilihDownload Free PDFView PDFProsiding Konferensi Nasional Sistem Informasi 2016Muhammad RopiantoProsiding Konferensi Nasional Sistem Informasi 2016  Menjembatani antara Teori dan Implementasi Sistem Informasi untuk Memperkuat Daya Saing Bangsa dalam Era Masyarakat Ekonomi ASEAN MEA  Kampus STT Ibnu Sina Batam 1113 Agustus 2016Download Free PDFView PDFMODEL ARSITEKTUR ENTERPRISE UNTUK MENDUKUNG SISTEM INFORMASI PADA STT IBNU SINA BATAMMuhammad RopiantoMeningkatnya pertumbuhan mahasiswa sekolah tinggi teknik ibnu sina Batam dan ketatnya persaingan bisnis diantar perguruan tinggi di Indonesia mendorong stakeholder untuk memberikan pelayanan yang sebaikbaiknya termasuk penyediaan sistem informasi Analisa dan perancangan sistem informasi sangat diperlukan Arsitektur pada data sistem dan teknologi informasi sangat diperlukan untuk membuat sistem yang dapat diandalkan Metode Enterprise Architectur Planning EAP merupakan metode yang dapat digunakan untuk mendesian sistem informasi yang dapat diandalkan sesuai dengan kebutuhan STT Ibnu Sina BatamPendefinisian arsitektur enterprise pada STT Ibnu Sina Batam ditemukan 32 entitas dan 28 usulan sistem informasiDownload Free PDFView PDFJurusan Teknik Informatika dan Sistem InformasiPenyusunan Sistem Evaluasi Kinerja Layanan Dalam Membangun Tata Kelola TI Berbasis Komputasi Awan Maret 20162016  Norbertus Tri Suswanto SaptadiEngineering models design on performance application is expected to contribute to the development of IT governance system in the hospital Engineering models are developed using a framework standard As public facility in the area of health hospital management requires performance services application to identify the needs of stakeholders Services performance application design require a good step in the preparation thus it takes study of relevant theory The methods in the study of the theory is the TOGAF ADM approach The presence of cloud computing technology can support operational activities at the hospital The challenge is how hospitals can adopt the technology An effective strategy derived from the results of the services performance evaluation therefore the use of technology can create effective and efficient IT governance from financial positions The method used in compiling the IT governance strategy is the system architecture which includes interface design infrastructure management classification definition and connectivity design The main components include business architecture information data applications and technologies The result of engineering models design have shown that hospitals can use it as a standard architecture model based on a structured system with support from cloud computing technology Keywordsperformance services IT governance TOGAF ADM cloud computingDownload Free PDFView PDFKonferensi Nasional Ilmu Komputer KONIK 2016KONSEP DAN DESAIN ARSITEKTUR JARINGAN TEKNOLOGI INFORMASI UNTUK PENERAPAN SMART CITY STUDI KASUS KOTA KENDARI SULAWESI TENGGARA2016  Muhammad Nadzirin Anshari NurSaat ini banyak kota besar dan berkembang menerapkan konsep smart city untuk meningkatkan pembangunan dan pelayanan kepada masyarakat termasuk kota kendari sulawesi tenggara untuk mewujudkan hal tersebut dibutuhkan infrastruktur jaringan teknologi informasi yang menghubungkan instansi pemerintahan dan fasilitas perkotaan yang menunjang smart city salah satu hal penting dalam penyediaan infrastruktur jaringan adalah pematangan konsep dan desain arsitektur jaringan teknologi informasi penelitian dilakukan dengan mengumpulan data tentang kondisi infrastruktur jaringan yang ada saat ini kemudian membuat konsep dan desain berdasarkan pemetaan wilayah instansi di setiap kecamatan yang ada di kota kendari Kata Kunci Arsitektur Tecknologi informasi Model Smart CityDownload Free PDFView PDFKNSI2014346 PENERAPAN STEGANOGRAFI METODE END OF FILE EOF DAN ENKRIPSI METODE DATA ENCRYPTION STANDARD DES PADA APLIKASI PENGAMANAN DATA GAMBAR BERBASIS JAVA PROGRAMMINGRuben TampubolonAbstrak Terdapat beberapa cara untuk menangani masalah keamanan data rahasia yang dikirimkan melalui internet diantaranya adalah menggunakan teknik kriptografi dan steganografi Steganografi merupakan ilmu dan seni penyembunyian informasipesan pada suatu media sedemikian rupa sehingga keberadaannya tidak terdeteksi oleh pihak lain yang tidak berhak atas informasi tersebut Sebaliknya kriptografi menyamarkan arti dari suatu pesan tapi tidak menyembunyikan bahwa ada suatu pesan karena file terlihat mencurigakan Teknik Steganografi yang penulis gunakan adalah End Of File EOF Teknik EOF menggunakan cara menambahakan data atau file pada akhir file image Untuk teknik ini data atau file yang akan disembunyikan besar ukurannya dapat melebihi dari ukuran file image Data yang disembunyikan tersebut akan disisipkan pada akhir file sehingga tidak akan mempengaruhi gambar Aplikasi steganografi ini juga dilengkapi dengan fungsi kriptografi Data Encryption Standard DES pada saat penyisipan data yang berfungsi sebagai kode pembangkit dan mengenkripsi data agar keamanan suatu data dalam file lebih terjaga dan terlindungi dari pihak yang tidak berhak mengetahui data tersebut Jogjack Factory outlet merupakan usaha dagang yang bergerak dibidang fashion Selain menjual Factory Outlet ini mendesain dan memproduksi sendiri barang dagangannya Desain yang dikirim sangat rahasia dan tidak boleh diterima oleh pihak lain Dengan dikembangkan sebuah sistem dengan mengimplementasikan sistem keamanan data menggunakan steganografi dengan algoritma metode end of file EOF dan enkripsi data standard DES berbasis Java Programming diharapkan dapat melindungi data rahasia perusahaan agar tidak mudah terbaca oleh orang yang tidak berkepentinganDownload Free PDFView PDFProceeding Konferensi Nasional Ilmu Komputer 2014Rancang Bangun Aplikasi Layanan Informasi Wisata Budaya Yogyakarta Berbasis Mobile Web dan LocationBased Service Secara KolaboratifKusworo AninditoYogyakarta merupakan salah satu kota yang memiliki potensi pariwisata yang beragam Potensi wisata tersebut antara lain keindahan alam peninggalan sejarah kuliner dan budaya Jika potensi ini dapat dioptimalkan maka akan dapat membantu meningkatkan kondisi perekonomian daerah di sekitar potensi wisata tersebut Promosi wisata budaya Yogyakarta belum banyak dilakukan Kegiatan promosi wisata dapat dilakukan dengan memanfaatkan perkembangan teknologi khususnya teknologi piranti mobile Aplikasi pengumpulan dan penyampaian informasi wisata budaya Yogyakarta yang akan dikembangkan merupakan aplikasi berbasis mobile web agar dapat diakses melalui berbagai piranti khususnya piranti mobile tanpa terikat platform dari piranti yang digunakan Pemuktahiran informasi mengenai wisata budaya ini dilakukan secara kolaboratif agar informasi lebih cepat terkumpul Aplikasi ini juga menyediakan locationbased service agar orang yang tertarik untuk mempelajari budaya Yogyakarta dapat dipandu mencapai lokasinya dengan mudah Dengan adanya sistem ini diharapkan semakin banyak orang yang terlibat untuk berbagi informasi serta semakin tertarik untuk lebih mengenal budaya YogyakartaDownload Free PDFView PDFPengembangan Sistem ETracer Study pada Perguruan TinggiReza ChandraEvaluasi terhadap kompetensi yang dibutuhkan oleh dunia kerja sangat diperlukan oleh perguruan tinggi agar tidak terdapat jarak antara dunia pendidikan tinggi dengan dunia kerja nyata yang ada di masyarakat Kendala yang dihadapi oleh perguruan tinggi dalam melakukan tracer study adalah pada saat pengumpulan data Beberapa perguruan tinggi masih melakukan pengumpulan data secara manual dengan cara menyebar kertas kuisioner dan wawancara melalui telepon terhadap alumni dan perusahaan Oleh karena itu diperlukan suatu Pengembangan layanan ETracer Study yang lengkap yang dapat memberikan informasi bagi perguruan tinggi untuk kepentingan perbaikan kurikulum penelusuran alumni secara detail serta mengetahui kepuasan pengguna lulusan perguruan tinggiDownload Free PDFView PDFKonferensi Nasional Sistem Informasi 2014 STMIK Dipanegara MakassarPENERAPAN STEGANOGRAFI METODE END OF FILE EOF DAN ENKRIPSI METODE DATA ENCRYPTION STANDARD DES PADA APLIKASI PENGAMANAN DATA GAMBAR BERBASIS JAVA PROGRAMMING2014  Dolly Virgian Shaka Yudha SaktiTerdapat beberapa cara untuk menangani masalah keamanan data rahasia yang dikirimkan melalui internet diantaranya adalah menggunakan teknik kriptografi dan steganografi Steganografi merupakan ilmu dan seni penyembunyian informasipesan pada suatu media sedemikian rupa sehingga keberadaannya tidak terdeteksi oleh pihak lain yang tidak berhak atas informasi tersebut Sebaliknya kriptografi menyamarkan arti dari suatu pesan tapi tidak menyembunyikan bahwa ada suatu pesan karena file terlihat mencurigakan Teknik Steganografi yang penulis gunakan adalah End Of File EOF Teknik EOF menggunakan cara menambahakan data atau file pada akhir file image Untuk teknik ini data atau file yang akan disembunyikan besar ukurannya dapat melebihi dari ukuran file image Data yang disembunyikan tersebut akan disisipkan pada akhir file sehingga tidak akan mempengaruhi gambar Aplikasi steganografi ini juga dilengkapi dengan fungsi kriptografi Data Encryption Standard DES pada saat penyisipan data yang berfungsi sebagai kode pembangkit dan mengenkripsi data agar keamanan suatu data dalam file lebih terjaga dan terlindungi dari pihak yang tidak berhak mengetahui data tersebut Jogjack Factory outlet merupakan usaha dagang yang bergerak dibidang fashion Selain menjual Factory Outlet ini mendesain dan memproduksi sendiri barang dagangannya Desain yang dikirim sangat rahasia dan tidak boleh diterima oleh pihak lain Dengan dikembangkan sebuah sistem dengan mengimplementasikan sistem keamanan data menggunakan steganografi dengan algoritma metode end of file EOF dan enkripsi data standard DES berbasis Java Programming diharapkan dapat melindungi data rahasia perusahaan agar tidak mudah terbaca oleh orang yang tidak berkepentinganDownload Free PDFView PDFSee Full PDFDownload PDFLoading PreviewSorry preview is currently unavailable You can download the paper by clicking the button aboveRELATED PAPERSKNSI2014381 Studi Dan Implementasi Algoritma Terinspirasi Sistem Imun  Clonal Selection Algorithmiping suprianaDownload Free PDFView PDFMODEL KNOWLEDGE MANAGEMENT PADA PERUSAHAAN DISTRIBUTOR FARMASI DAN CONSUMER PRODUCTasep id hadianaDownload Free PDFView PDFProsiding SNIf 2015helmi kurniawan Santi S Uyock Saputro Alimuddin Yasin iko rasaki INDRA SAMSIE Isnanto Adi Prasetyo Ni Kadek Sumiari Ni Ketut Dewi Ari Jayanti Nova Rijati AnNa NaTsirDownload Free PDFView PDFKonferensi Nasional Sistem Informasi KNSISistem Informasi Manajemen Ruang Kuliah Berbasis Piranti Bergerak2014  Rendra Gustriansyah Nazori SuhandiDownload Free PDFView PDFLAPORAN AKHIR P2M PENERAPAN IPTEKSA Shodiqul Amiin RosyidDownload Free PDFView PDFKonferensi Nasional Sistem Informasi 2014 STMIK Dipanegara MakassarPendekatan UML dalam Perancangan Sistem Informasi Online Presensi Mahasiswa2014  Rushendra RustamDownload Free PDFView PDFAnalisis tingkat kepuasan mahasiswa atas layanan akademik berbasis web UGyani shuDownload Free PDFView PDFDigital Library Modeling Using UML For Supporting Knowledge ManagementAry Budi WarsitoDownload Free PDFView PDFPoliteknik Negeri Ujung Pandang dengan BBPPKI Makassar KOMINFOModel Antarmuka Evaluasi Kinerja Layanan Berbasis Arsitektur Komputasi Awan Untuk Membangun Strategi Tata Kelola TI Juni 20152015  Norbertus Tri Suswanto Saptadi Hans MarwiDownload Free PDFView PDFJurnal HOAQ  Teknologi Informasi STIKOM Uyelindo KupangPERANCANGAN PENJADWALAN KULIAH STIKOM UYELINDO DENGAN ALGORITMA GENETIK2014  Marinus Ignasius J A W A W U A N LamabelawaDownload Free PDFView PDFFakultas Teknologi Informasi Universitas Atma Jaya MakassarPerancangan Aplikasi Evaluasi Kinerja Berdasarkan Kerangka Kerja TOGAF ADM Untuk Membangun Tata Kelola Teknologi Informasi September 20152015  Norbertus Tri Suswanto Saptadi Hans MarwiDownload Free PDFView PDFKonferensi Nasional Sistem dan Informatika KNSIRancang Bangun Model Layanan Fungsi Menggunakan Data Warehouse Dalam Penyusunan Blueprint Rumah Sakit November 20142014  Norbertus Tri Suswanto Saptadi Hans MarwiDownload Free PDFView PDFProsiding Konferensi Nasional Pengembangan Teknologi Informasi dan Komunikasi KeTIK 2014Irwan Nasution Dedy Hartama Dosen Yahfiz Gortap Lumbantoruan Indraedy Syahputra Hildayati RaudahDownload Free PDFView PDFKNSI 2015PEMILIHAN PERANGKAT PEMROSESAN DATA2016  Faisal PiliangDownload Free PDFView PDFPerancangan Sistem ECommerce Untuk Memperluas Pasar Produk OlehOleh Khas PontianakKurniya FernandoDownload Free PDFView PDFPrediksi Kelulusan Mahasiswa Pada Perguruan Tinggi Kabupaten Majalengka Berbasis Knowledge Based SystemDony SusandiDownload Free PDFView PDFKonferensi Nasional Sistem Informasi KNSI 2014MODEL SISTEM EXECUTIVE DIGITAL DASHBOARD UNTUK PERGURUAN TINGGI2014  henderi syafeiDownload Free PDFView PDFPoliteknik Negeri Ujung Pandang dengan BBPPKI Makassar KOMINFOEngineering Models Design On Performance Application Using TOGAF ADM In Developing IT Governance Strategy Juni 20152015  Norbertus Tri Suswanto SaptadiDownload Free PDFView PDFGaleri Online Kesenian MinangIrwan NasutionDownload Free PDFView PDFSeminar Nasional Informatika SNIf  2014Fitri Nuraeni II Anggit Dwi Hartanto Khairul Ummi Rita N O V I T A Sari tatik just Charles Sianturi helmi kurniawan Sandy KosasiDownload Free PDFView PDFKonferensi Nasional Ilmu Komputer ISBN 9786029856309Analisis Kebutuhan Open Source Software pada Universitas Atma Jaya Makassar Januari 20122012  Norbertus Tri Suswanto SaptadiDownload Free PDFView PDFUniversitas De La Salle ManadoPenyusunan Good IT Governance Berdasarkan Kajian Teori Cloud Computing Menggunakan Model Rekayasa Sistem April 20172017  Norbertus Tri Suswanto SaptadiDownload Free PDFView PDFSeminar Nasional Informatika SNIf 2014pdfIwan Fitrianto Rahmad Ni Ketut Dewi Ari Jayanti S Yuswanto Gede Suardika Ni Kadek Sumiari muhammad rusdi tanjung Vidi AgoengDownload Free PDFView PDFDESAIN PENGATURAN BANDWIDTH LEWAT JARINGAN LOCAL AREA NETWORKING AD HOC UNTUK INTEGRASI INFORMASI SISTEM INFORMASI DAERAH KOTA MATARAMM Zainal ArifinDownload Free PDFView PDFPerancangan sistem ecommerce untuk produk pembuatan kueTAFFAQUH VIDEODownload Free PDFView PDFSeminar Nasional Informatika ISSN 20889047Analisis Penggunaan Teknologi Informasi Pada Rumah Sakit Stella Maris Makassar Oktober 20122012  Norbertus Tri Suswanto SaptadiDownload Free PDFView PDF485 KNSI2014294 3 DIMENSI MODELING CHARACTER HEWAN BERKAKI EMPAT DENGAN METODE RIGGINGmuhammad rusdi tanjungDownload Free PDFView PDFTRILOGIHALAMAN ELEKTRONIK MEDIA PROMOSI2015  Faisal PiliangDownload Free PDFView PDFSeminar Nasional Riset dan Teknologi Terapan VI RitektraPenyusunan Good IT Governance Berdasarkan Kajian Teori Cloud Computing Menggunakan Model Rekayasa Sistem Agustus 20162016  Norbertus Tri Suswanto SaptadiDownload Free PDFView PDFSeminar Nasional APTIKOM SEMNASTIKOMRANCANGAN DATA WAREHOUSE UNTUK ANALISIS KINERJA PRODUKSI DI PT URECEL INDONESIA2016  bayu pramono Ahmad RoihanDownload Free PDFView PDFUniversitas Muhamadiyah Malang UMM Jawa TimurServices Performance Evaluation Interface Model Of Cloud Computing Based Architecture To Build Strategic IT Governance Juni 20152015  Norbertus Tri Suswanto Saptadi Hans MarwiDownload Free PDFView PDFProsiding SESINDO 2015  FixpdfM Zainal ArifinDownload Free PDFView PDFSeminar Nasional Informatika SNIf   2013Irwan Nasution Teuku Mufizar helmi kurniawanDownload Free PDFView PDFPROSIDING Seminar Nasional Inovasi dan Teknologi Informasi 2015 SNITI 2015 Tema Pemberdayaan Kearifan Lokal Melalui Inovasi Teknologi Informasi DidukungJeperson HutahaeanDownload Free PDFView PDFbukuabstrakpdfSEMANTIK UDINUSDownload Free PDFView PDFKNSI2014370 Kajian Teori Flow Sebagai Sumber Motivasi Belajar DI Serious Gameiping suprianaDownload Free PDFView PDFKONSEPSI PENGEMBANGAN SISTEM INFORMASI DENGAN DUKUNGAN SISTEM INTELIGEN Keynote Paper KNSI 20142014  iping suprianaDownload Free PDFView PDFPENGGUNAAN TEORI INSTITUSIONAL DALAM PENELITIAN TEKNOLOGI INFORMASI DAN KOMUNIKASI DI INDONESIAPutri IsmaidaDownload Free PDFView PDFProdi Teknik Informatika Jurusan Teknik Elektro Universitas HasanuddinAnalisis Penggunaan Teknologi Informasi Dalam Perspektif CRM EIS Dan DSS September 20132013  Norbertus Tri Suswanto Saptadi Hans MarwiDownload Free PDFView PDFPROSIDING SNITI 2017 FULL FINALpdfPAS MARTODownload Free PDFView PDFRELATED TOPICSAplikasiSee Full PDFDownload PDFAboutPressBlogPeoplePapersTopicsJob Board Were Hiring Help CenterFind new research papers inPhysicsChemistryBiologyHealth SciencesEcologyEarth SciencesCognitive ScienceMathematicsComputer ScienceTermsPrivacyCopyrightAcademia 2023"

similarity, significant_features = calculate_text_similarity(text1, text2)
print("Similarity Score:", similarity)
print("Top 5 Significant Features:")
top_5_features = sorted(significant_features, key=lambda x: x[1], reverse=True)[:5]
# top_5_features = sorted(significant_features, key=lambda x: x[1], reverse=True)
for feature, weight in top_5_features:
    # print(f"- {feature}: {weight}")
    print("- "+feature + ": "+str(round(weight*100,2))+"%")
