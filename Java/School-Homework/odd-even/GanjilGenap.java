import java.util.Scanner;
import java.util.Arrays;

public class GanjilGenap {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		int willRepeat;

		do {
			int[] bilangan;
			int whileLoop, squaroot;
			char repeatQ;

			bilangan = new int[2];
			for(int i=0; i<2; i++) {
				System.out.println("Input bilangan ke-"+ (i+1) +": ");
				bilangan[i] = input.nextInt();
			}

			System.out.println("");
			System.out.println("============================================");
			System.out.println("");

			// System.out.println(Arrays.toString(prime_num));
			for (int j=bilangan[0]; j <= bilangan[1]; j++) {
				// System.out.println( (int) akar + 1 );
				// System.out.println(prime_num[j]);
				// System.out.println(akar + "=" + prime);
				squaroot = (int) Math.pow(j, 0.5) + 1;
				System.out.println(j +","+squaroot+"="+(squaroot % j));
				if (j % 2 == 0) {
					System.out.print(j + "  Bilangan Genap");
				} else {
					System.out.print(j + "  Bilangan Ganjil");
				}
				for (int k = 0; k <= squaroot; k++) {
					if (j % squaroot == k) {
						System.out.println(" (Prima)");
						k = squaroot;
					} else {
						System.out.println();
						k = squaroot;
					}
				}
			}

			System.out.println("Apakah mau mencoba data yang lain? (Y/n) ");
			willRepeat = input.next().charAt(0);
			willRepeat = Character.toUpperCase(willRepeat);

		} while(willRepeat=='Y');
	}
}
