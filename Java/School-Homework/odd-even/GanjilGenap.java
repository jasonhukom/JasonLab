import java.util.Scanner;
import java.util.Arrays;

public class GanjilGenap {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		int willRepeat;
		do {
			int[] bilangan;
			int whileLoop;
			char repeatQ;

			bilangan = new int[1];
			bilangan = new int[2];
			bilangan = new int[3];

			for(int i=0; i<2; i++) {
				System.out.println("Input bilangan ke-"+ (i+1) +": ");
				bilangan[i] = input.nextInt();
			}
			for (int j=bilangan[0]; j < bilangan[1]; j++) {
				// System.out.println("THIS WORKS");
				double akar = Math.pow(j, 0.5);
				System.out.println( (int) akar + 1);
				if (j == (int) akar + 1){
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
