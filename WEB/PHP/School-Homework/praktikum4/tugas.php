    <?php
        echo "<h2>Hitung Nilai Akhir Siswa</h2>";
        function hitungNilaiAkhir($tugas, $uts, $uas) {
            $tugas  *= 0.2;
            $uts    *= 0.3;
            $uas    *= 0.5;
            $nilai_akhir = $tugas + $uts + $uas;
            return $nilai_akhir;
        }

        $data_siswa = [
            ["nama"=>"Jason","tugas"=>85,"uts"=>89,"uas"=>87],
            ["nama"=>"Nicholas","tugas"=>95,"uts"=>80,"uas"=>78],
            ["nama"=>"Wesley","tugas"=>89,"uts"=>90,"uas"=>95]
        ];

        echo "
        <table border='1' cellpadding='5'>
            <tr>
                <th>No.</th>
                <th>Nama</th>
                <th>Tugas</th>
                <th>Ujian Tengah Semester</th>
                <th>Ujian Akhir Semester</th>
                <th>Nilai Akhir</th>
            </tr>";

        foreach ($data_siswa as $index => $isi) {
            $no = $index + 1;
            $nilai_akhir = hitungNilaiAkhir($isi["tugas"],$isi["uts"],$isi["uas"]);
            echo "
                <tr>
                    <th>$no</th>
                    <th>$isi[nama]</th>
                    <th>$isi[tugas]</th>
                    <th>$isi[uts]</th>
                    <th>$isi[uas]</th>
                    <th>$nilai_akhir</th>
                </tr>";
            }
        echo "</table>";

    ?>

