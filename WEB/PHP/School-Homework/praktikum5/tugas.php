<!DOCTYPE html>
<html lang="en">
<head>
    <title>Data Siswa</title>
</head>
<body>
    <?php
        echo "<h2> Siswa dan nilainya </h2>";
        $siswa = [
            ["nama"  => "Jason Christopher Hukom","nilai" => 84],
            ["nama"  => "Aizat Fahim Firmansyah","nilai" => 95],
            ["nama"  => "Josua Bagus Rusidianto","nilai" => 89],
            ["nama"  => "Satrio Ernesto Utomo","nilai" => 90],
            ["nama"  => "Devon Christan Setiawan","nilai" => 85]
            ];

        foreach ($siswa as $index => $isi) {
            $no = $index + 1;
            echo "<h3>$no. Nama: $isi[nama] <br></h3>";
            echo "Nilai: $isi[nilai] <br>";
        }
    ?>
    
</body>
</html>