<?php
    echo "<h1>Predikat Nilai</h1>";
    $dpk = 90;
    $komputer = 87;
    $pw = 100;
    
    $rata_rata = ($dpk + $komputer + $pw) / 3;

    if ($rata_rata >= 90) {
        $predikat = "A";
    } elseif ($rata_rata >= 80) {
        $predikat = "B";
    } elseif ($rate_rate >= 70) {
        $predikat = "C";
    } else {
        $predikat = "D";
    }

    echo "Nilai DPK             : $dpk <br>";
    echo "Nilai Komputer        : $komputer <br>";
    echo "Nilai Pemrograman Web : $pw <br>";
    echo "Rata-rate             : $rata_rata <br>";
    echo "Predikat              : $predikat <br>     ";
?>