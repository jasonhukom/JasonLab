<?php
    function tambah($angka1, $angka2) {
        return $angka1 + $angka2;
    }
    
    function kurang($angka1, $angka2) {
        return $angka1 - $angka2;
    }

    function kali($angka1, $angka2) {
        return $angka1 * $angka2;
    }

    function bagi($angka1, $angka2) {
        return $angka1 / $angka2;
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h2>Sonculator</h2>
    <form action="" method="POST">
        Angka 1 : <input type="number" name="angka1" required><br><br>
        Angka 2 : <input type="number" name="angka2" required><br><br>
        Operator:
        <input type="submit" name="operator" value="+">
        <input type="submit" name="operator" value="-">
        <input type="submit" name="operator" value="*">
        <input type="submit" name="operator" value="/"><br><br>
    </form>

    <?php
    if (isset($_POST['operator'])) {
        $angka1 = htmlspecialchars($_POST['angka1']);
        $operator = htmlspecialchars($_POST['operator']);
        $angka2 = htmlspecialchars($_POST['angka2']);
        
        echo "Hasil: ";
        if ($operator == "+") {
            echo "$angka1 + $angka2 = " . tambah($angka1, $angka2);
        } elseif ($operator == "-") {
            echo "$angka1 - $angka2 = " . kurang($angka1, $angka2);
        } elseif ($operator == "*") {
            echo "$angka1 * $angka2 = " . kali($angka1, $angka2);
        } elseif ($operator == "/") {
            echo "$angka1 / $angka2 = " . bagi($angka1, $angka2);
        } else {
            echo "Operator Aritmatika salah!";
        }  
    }
?>

</body>
</html>