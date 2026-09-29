<?php
    include "koneksi.php";
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $nama = $_POST['nama'];
        $kelas = $_POST['kelas'];
        $nilai = $_POST['nilai'];

        mysqli_query($koneksi, "INSERT INTO siswa (nama, kelas, nilai) VALUES ('$nama', '$kelas', '$nilai')");
        header("Location: tampil.php");
    }
?>
<form method="POST">
    Nama : <input type="text" name="nama"><br>
    Kelas : <input type="text" name="kelas"><br>
    Nilai : <input type="number" name="nilai"><br>
    <input type="submit" value="Simpan">
</form>