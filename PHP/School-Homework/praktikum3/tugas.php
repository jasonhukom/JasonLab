<?php
    echo "<h1>Ganjil Genap</h1>";
    for ($i = 1; $i <= 20; $i++) {
        echo "<br>";
        if ($i % 3 == 0) {
            continue;
        }
        if ($i % 2 == 0) {
            echo "$i Angka Genap";
        } else {
            echo "$i Angka Ganjil";
        }
    }
?>