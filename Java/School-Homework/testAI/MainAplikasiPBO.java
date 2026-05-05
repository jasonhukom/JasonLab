//import java.util.Scanner;

//Scanner input = new Scanner(System.in);

// Parent Class (Superclass)
class bendaSekolah {
    String nama;
    int lenNama;
    String format_table;
    
    bendaSekolah(String nama) {
        this.nama = nama;
        lenNama = nama.length();
        format_table = "| %-14s | %-" + lenNama + "s |%n";
    }
    
    void deskripsi() {
        System.out.println("┌────────────────┬" + ("─".repeat(lenNama)) + "──┐");
        System.out.printf(format_table, "Nama Benda", nama);
        System.out.println("└────────────────┴" + ("─".repeat(lenNama)) + "──┘");
    }
}

// 1. Class Terminal Stop Kontak
class terminalStopKontak extends bendaSekolah {
    int jumlahLobang;
    String warna;
    String kondisiKabel;

    terminalStopKontak(int jml, String w, String k) {
        super("Terminal Stop Kontak");
        this.jumlahLobang = jml;
        this.warna = w;
        this.kondisiKabel = k;
    }

    void salurkanListrik() {
        System.out.println("Status: Menyalurkan listrik melalui " + jumlahLobang + " lubang.");
    }
}

// 2 Air kolam
class airKolam extends bendaSekolah {
    String warna;
    String kondisi;
    String jenisAir;

    airKolam(String w, String k, String j) {
        super("Air Kolam");
        this.warna = w;
        this.kondisi = k;
        this.jenisAir = j;
    }

    void mengalirkanListrik() {
        System.out.println("Status: Air kolam berwarna " + warna + " dengan kondisi " + kondisi + ", jenis air " + jenisAir + " kemungkinan bisa mengantarkan arus listrik.");
    }
}

// 3 Class Wastafel
class wastafel extends bendaSekolah {
    String warnaKatup;
    boolean airMengalir = false;

    wastafel(String katup) {
        super("Wastafel");
        this.warnaKatup = katup;
    }

    void bukaKeran() {
        airMengalir = true;
        System.out.println("Status: Keran " + warnaKatup + " dibuka. Air mengalir ke tadah.");
    }
}

// 3. Class Pohon
class pohon extends bendaSekolah {
    String warnaDaun;
    String kondisi;

    pohon(String w, String k) {
        super("Pohon Sekolah");
        this.warnaDaun = w;
        this.kondisi = k;
    }

    void fotosintesis() {
        System.out.println("Proses: Pohon " + kondisi + " sedang menyerap CO2 dan menghasilkan Oksigen.");
    }
}

// Main Class untuk menjalankan program
public class MainAplikasiPBO {
    public static void main(String[] args) {
        
        // Membuat Objek berdasarkan hasil observasi kalian
        terminalStopKontak terminal1 = new terminalStopKontak(4, "Putih", "Bagus");
        wastafel wastafelKantin = new wastafel("Merah");
        pohon pohonMangga = new pohon("Hijau Muda", "Sehat");

        // Menjalankan Operasi (Method)
        terminal1.deskripsi();
        terminal1.salurkanListrik();

        System.out.println();

        wastafelKantin.deskripsi();
        wastafelKantin.bukaKeran();

        System.out.println();

        pohonMangga.deskripsi();
        pohonMangga.fotosintesis();
        
        System.out.println("\n-------------------------------------------");
        System.out.println("Laporan Kelompok: Devon, Jason, Josua, Satrio");
        System.out.println("PPLG B - SMKN 2 SURAKARTA");
    }
}
