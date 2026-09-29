<!DOCTYPE html>
<html>
<head>
    <title>Siswa Daftar</title>
</head>
<body>
    <h2> Daftar Siswa </h2>
    <?php
        $nama = "SON😭🙏";
        $kelas = "XI RPL B";
        $nilai_uts = 85;
        $nilai_uas = 90;
        $rata_rata = ($nilai_uts + $nilai_uas) / 2;
        $lulus = $rata_rata >= 75;

        echo "Nama              : $nama <br>";
        echo "Kelas             : $kelas <br>";
        echo "Rata-rata         : $rata_rata <br>";
        echo "Status Kelulusan  : ";
        echo $lulus ? "LULUS" : "TIDAK LULUS";
        
        echo "<br><br><br>";
    ?>
</body>
</html>