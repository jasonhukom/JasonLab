<?php
    $siswa = ["Jason", "Aizat", "Josua", "Satrio"];

    echo "<h3> Daftar Nama Siswa</h3>";
    foreach ($siswa as $index => $nama) {
        $no = $index + 1;
        echo "$no. $nama <br>";
    }

    echo "<br>";

    // Array asosiatif
    $biodata = [
        "nama" => "Devon",
        "kelas" => "XI PPLG B",
        "hobi" => "Main Game"
    ];
    echo "Nama: " . $biodata["nama"];
?>
