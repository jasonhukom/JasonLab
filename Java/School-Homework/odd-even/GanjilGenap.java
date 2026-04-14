import java.util.Scanner;
import java.util.Arrays;

public class GanjilGenap {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		int willRepeat;
		do {
			int[] bilangan;
			boolean[] prime_num;
			int whileLoop;
			char repeatQ;

			bilangan = new int[2];
			for(int i=0; i<2; i++) {
				System.out.println("Input bilangan ke-"+ (i+1) +": ");
				bilangan[i] = input.nextInt();
			}

			System.out.println("");
			System.out.println("============================================");
			System.out.println("");

			prime_num = new boolean[bilangan[1]];
			for (int k=bilangan[0]; k <= bilangan[1]; k++) {
				boolean prime;
				double akar = Math.pow(k, 0.5);
				System.out.println(akar + "<" + k-1 + "=" 
				if (akar < k-1) {
					prime_num[k-(k-1)] = false;
				} else {
					prime_num[k-(k-1)] = true;
				}
			}
			System.out.println(Arrays.toString(prime_num));
			for (int j=bilangan[0]; j <= bilangan[1]; j++) {
				// System.out.println( (int) akar + 1 );
				// System.out.println(prime_num[j]);
				// System.out.println(akar + "=" + prime);
				if (prime_num[j-(j-1)]) {
					System.out.println(j + "  Bilangan Prima");
				} else if (j % 2 == 0) {
					System.out.println(j + "  Bilangan Genap");
				} else {
					System.out.println(j + "  Bilangan Ganjil");
				}
			}

			System.out.println("Apakah mau mencoba data yang lain? (Y/n) ");
			willRepeat = input.next().charAt(0);
			willRepeat = Character.toUpperCase(willRepeat);

		} while(willRepeat=='Y');
	}
}
