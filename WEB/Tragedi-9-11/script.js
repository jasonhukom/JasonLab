console.log("Tragedi September 9 2001");
// Membuat Variabel untuk menyimpan nama travel
// let peristiwaKejadian = "Tragedi September 11 2001";
// Memunculkan Pop-up Alert di layar
// alert("Selamat Datang di web tidak resmi " + peristiwaKejadian + "!");

const tombolPesan   = document.getElementById('tombol-pesan');
const tombolTema    = document.getElementById('tombol-tema');
const bodyHalaman   = document.getElementById('halaman-utama');

tombolPesan.addEventListener('click', function() {
    alert('Terimakasih untuk feedbacknya!');
});

tombolTema.addEventListener('click', function() {
    bodyHalaman.classList.toggle('dark-mode');
});