import java.util.Scanner;

public class materi_array {
	public static void  main(String [] args) {
		Scanner input = new Scanner(System.in);
		int [] nilai;

		System.out.println("Input jumlah index dalam array: ");
		nilai = new int[input.nextInt()];
		int jumlahElement = nilai.length;
		System.out.println("Jumlah element: " + jumlahElement);

		System.out.println();

		for (int j = 0; j < jumlahElement; j++) {
			System.out.print("Masukan input ke dalam array[" + j + "]: ");
			nilai[j] = input.nextInt();
		}

		System.out.println();

		System.out.print("{");
		for (int i = 0; i < jumlahElement; i++) {
			System.out.print(nilai[i]);
			if (i != jumlahElement - 1) {
				System.out.print(", ");
			}
		}
		System.out.println("}");
	}
}
