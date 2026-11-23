import java.util.Scanner;

class BendaSekolah {
	String nama;

	BendaSekolah(String nama) {
		this.nama = nama;
	}

	void deskripsi() {
		System.out.println("--- Mengamati Objek: " + nama + " ---");
	}

class terminalStopKontak extends BendaSekolah {
	int jumlahLobang;
	String warna, posisi, kondisi;

	terminalStopKontak(int jmlh, String w, String pos, String k) {
		jumlahLobang = jmlh;
		warna = w;
		posisi = pos;
		kondisi = k;
	}

	void salurkanListrik() {
		
	}
}
}
