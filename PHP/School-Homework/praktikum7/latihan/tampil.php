<?php
    include "koneksi.php";
    $query = mysqli_query($koneksi, "SELECT * FROM siswa");
?>
<table border="1" cellpadding="8">
    <tr><th>No</th><th>Nama</th><th>Kelas</th><th>Nilai</th></tr>
    <?php $no = 1; while ($data = mysqli_fetch_array($query)) { ?>
    <tr>
        <td><?= $no++ ?></td>
        <td><?= $data['nama'] ?></td>
        <td><?= $data['kelas'] ?></td>
        <td><?= $data['nilai'] ?></td>
    </tr>
    <?php } ?>
</table>