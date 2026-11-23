import java.util.Scanner;

public class bubblesort {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);

		int [] data;

		System.out.println("Length of array: ");
		int lenData = input.nextInt();
		data = new int[lenData];
		for (int i = 0; i < lenData; i++ ) {
			System.out.println("Data "+(i+1)+": ");
			outerLoop:
			while (true) {
				try {
					data[i] = input.nextInt();
					break outerLoop;
				} catch (Exception e) {
					System.out.println("Input mu error bro, skill issue");
				}
			}
		}

		for (int j = 0; j < lenData * lenData; j++) {
			try {
				int a = data[j];
				int b = data[j+1];
				if (a > b) {
					data[j] = b;
					data[j+1] = a;
				}
			} catch (Exception e) {}
		}

		System.out.println("SORTED");
		for (int k = 0; k < lenData; k++) {
			System.out.println(data[k]);
		}
	}
}
