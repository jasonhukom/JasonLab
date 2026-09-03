<!DOCTYPE html>
<html lang="en">
<head>
    <title>hitung tu persegi panjang lo</title>
</head>
<body>
    <h2>latihan PHP 3</h2>
    <?php
        function hitungLuasPersegiPanjang($panjang, $lebar) {
            $luas = $panjang * $lebar;
            return $luas;
        }

        $hasil = hitungLuasPersegiPanjang(12, 8);
        echo "Luas persegi panjang: $hasil";
    ?>
</body>
</html>