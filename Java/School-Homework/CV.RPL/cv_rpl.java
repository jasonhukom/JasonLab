import java.text.NumberFormat; // Rupiah Formatter
import java.util.Locale; // Rupiah Formatter
import java.util.Scanner;
import java.util.Arrays; // Array Stream
import java.util.Comparator; // Check Length or smth

public class cv_rpl {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);

		String name;
		int data, jumlah_anak;
		char golongan, status_nikah_yn, status_nikah_yn_upper;
		char golongan_upper = '-';
		boolean status_nikah_bool = false;

		double 	tunjangan_nikah, tunjangan_anak, gapok_nikah, gapok_anak, gaber;
		int gapok;

		int i,j,x,y,z;
		char loop;

		int jumlah_data = 7;

		// ARRAYS
		String[]  	name_arr, tunj_nikah_arr, tunj_anak_arr, gaber_arr, status_arr;
		char[] 		gol_arr;
		int[] 		jmlh_anak_arr;

		// FORMATTED
		String formatted_status_nikah;
		String formatted_tunjangan_nikah = "-";
		String formatted_tunjangan_anak = "-";
		String formatted_gaber = "-";

		do {
			System.out.println("Masukan jumlah data yang akan di input	: ");
			data = input.nextInt();
			name_arr	= new String[data];
			gol_arr		= new char[data];
			status_arr	= new String[data];
			jmlh_anak_arr	= new int[data];
			tunj_nikah_arr	= new String[data];
			tunj_anak_arr	= new String[data];
			gaber_arr	= new String[data];

			System.out.println("=====================================================");
			// Repeat Data
			for (i = 0; i < data; i++) {
				tunjangan_nikah = 0.1;
				tunjangan_anak  = 0.05;
				gapok = 0;
				gapok_nikah = 0.0;
				gapok_anak = 0.0;
				gaber = 0.0;
				jumlah_anak = 0;

				input.nextLine();
				// Input and Proccess
				System.out.println("Input Data "+(i+1)+": ");

				System.out.print("Masukkan Nama Karyawan		: ");
				name = input.nextLine();

				x = 1;
				while (x == 1) {
					System.out.print("Masukkan Golongan 		: ");
					golongan = input.next().charAt(0);
					golongan_upper = Character.toUpperCase(golongan);
					switch (golongan_upper) {
						case 'A':
							gapok = 1_000_000;
							x += 1;
							break;
						case 'B':
							gapok = 750_000;
							x += 1;
							break;
						case 'C':
							gapok = 500_000;
							x += 1;
							break;
						default:
							System.out.println("Input anda salah! Tolong input ulang");
							break;
					}
				}

				y = 1;
				while (y == 1) {
					System.out.print("Masukkan Status (Y/n)		: ");
					status_nikah_yn = input.next().charAt(0);
					status_nikah_yn_upper = Character.toUpperCase(status_nikah_yn);
					switch (status_nikah_yn_upper) {
						case 'Y':
							status_nikah_bool = true;
							gapok_nikah = tunjangan_nikah * gapok;
							y += 1;
							break;
						case 'N':
							status_nikah_bool = false;
							gapok_nikah = 0;
							y += 1;
							break;
						default:
							System.out.println("Input anda salah! Tolong input ulang");
							break;
					}
				}
				if (status_nikah_bool) {
					z = 1;
					while (z == 1) {
						System.out.print("Masukkan Jumlah Anak	: ");
						jumlah_anak = input.nextInt();
						if (jumlah_anak > 0) {
							if (jumlah_anak <= 4) {
								gapok_anak = tunjangan_anak * gapok  * jumlah_anak;
							} else if (jumlah_anak > 4) {
								gapok_anak = tunjangan_anak * gapok * 4;
							}
							z += 1;
						} else if (jumlah_anak ==  0) {
							gapok_anak = 0;
							z += 1;
						} else {
							System.out.println("Input anda salah! Tolong input ulang");
						}
					}
				}

				gaber = (double) gapok +  gapok_nikah + gapok_anak;

				// Format Nikah
				if (status_nikah_bool) {
					formatted_status_nikah = "Sudah Menikah";
				} else {
					formatted_status_nikah = "Belum Menikah";
				}

				// Format Tunjangan Anak dan Nikah
				//if (gapok_nikah >= 10_000_000) {
				//	formatted_tunjangan_nikah = "Rp." + ((int)gapok_nikah/10_000_000) + "0.000.000,00";
				//} else if (gapok_nikah >= 1_000_000) {
				//	formatted_tunjangan_nikah = "Rp." + ((int)gapok_nikah/1_000_000) + ".000.000,00";
				//} else if (gapok_nikah >= 100_000) {
				//	formatted_tunjangan_nikah = "Rp." + ((int)gapok_nikah/100_000) + "00.000,00";
				//} else if (gapok_nikah >= 10_000) {
				//	formatted_tunjangan_nikah = "Rp." + ((int)gapok_nikah/10_000) + "0.000,00";
				//} else {
				//	formatted_tunjangan_nikah = "-";
				//}

				//if (gapok_anak >= 10_000_000) {
				//	formatted_tunjangan_anak = "Rp." + ((int)gapok_anak/10_000_000) + "0.000.000,00";
				//} else if (gapok_anak >= 1_000_000) {
				//	formatted_tunjangan_anak  = "Rp." + ((int)gapok_anak/1_000_000) + ".000.000,00";
				//} else if (gapok_anak >= 100_000) {
				//	formatted_tunjangan_anak = "Rp." + ((int)gapok_anak/100_000) + "00.000,00;";
				//} else if (gapok_anak >= 10_000) {
				//	formatted_tunjangan_anak = "Rp." + ((int)gapok_anak/10_000) + "0.000,00";
				//} else {
				//	formatted_tunjangan_anak = "-";
				//}

				//if (gaber >= 10_000_000) {
				//	formatted_gaber = "Rp." + ((int)gaber/10_000_000) + "0.000.000,00";
				//} else if (gaber >= 1_000_000) {
				//	formatted_gaber = "Rp." + ((int)gaber/1_000_000) + ".000.000,00";
				//} else if (gaber >= 100_000) {
				//	formatted_gaber = "Rp." + ((int)gaber/10_000_000) + "000.000,00";
				//} else if (gaber >= 10_000) {
				//	formatted_gaber = "Rp." + ((int)gaber/10_000) + "0.000,00";
				//} else {
				//	formatted_gaber = "-";
				//}

				//AI
				Locale idrLocale = new Locale("in", "ID");
				NumberFormat rupiahFormat = NumberFormat.getCurrencyInstance(idrLocale);

				formatted_tunjangan_nikah = rupiahFormat.format(gapok_nikah);
				formatted_tunjangan_anak = rupiahFormat.format(gapok_nikah);
				formatted_gaber = rupiahFormat.format(gaber);

				name_arr[i]		= name;
				gol_arr[i]		= golongan_upper;
				status_arr[i]		= formatted_status_nikah;
				jmlh_anak_arr[i]	= jumlah_anak;
				tunj_nikah_arr[i]	= formatted_tunjangan_nikah;
				tunj_anak_arr[i]	= formatted_tunjangan_anak;
				gaber_arr[i]		= formatted_gaber;
			}
			System.out.println("=====================================================");
			System.out.println();

			// AI
			String longest = Arrays.stream(name_arr).max(Comparator.comparingInt(String::length)).orElse("");
			int maxLen = longest.length();

			// Output
			String longDash = "─".repeat(maxLen+2);
			String format = "│ %-5s │ %-" + maxLen + "s │ %-13s │ %-13s │ %-13s │ %-21s │ %-21s │ %-15s │%n";
			System.out.println("┌───────┬" + longDash + "┬───────────────┬───────────────┬───────────────┬───────────────────────┬───────────────────────┬─────────────────┐");
			System.out.printf(format, "No.", "Nama", "Golongan", "Status", "Jumlah Anak", "Tunjangan Suami/Istri", "Tunjangan Anak", "Gaber");
			System.out.println("├───────┼" + longDash + "┼───────────────┼───────────────┼───────────────┼───────────────────────┼───────────────────────┼─────────────────┤");
			for (j = 0; j < data; j++) {
			System.out.printf(format, (j+1), name_arr[j], gol_arr[j], status_arr[j], jmlh_anak_arr[j], tunj_nikah_arr[j], tunj_anak_arr[j], gaber_arr[j]);
			}
			System.out.println("└───────┴" + longDash + "┴───────────────┴───────────────┴───────────────┴───────────────────────┴───────────────────────┴─────────────────┘");
			System.out.println("Apakah anda mau input lagi? (Y/n) ");
			loop = input.next().charAt(0);
		} while (Character.toUpperCase(loop) == 'Y');
		input.close();
	}
}
