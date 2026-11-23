<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Struktur Control</title>
</head>
<body>
    <?php
        $nilai_uts = 78;
        
        if ($nilai_uts >= 90) {
            echo "Predikat A";
        } elseif ($nilai_uts >= 80) {
            echo "Predikat B";
        } elseif ($nilai_uts >= 70) {
            echo "Predikat C";
        } elseif ($nilai_uts >= 60) {
            echo "Predikat D";
        } else {
            echo "Predikat F";
        }

        echo "<h3>Tabel Perkalian 5</h3>";
        for ($i = 1; $i <= 10; $i++) {
        echo "5 x $i = " . (5 * $i) . "<br>";
        }
    ?>
</body>
</html>