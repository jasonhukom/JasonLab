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

		int j = 0;
		int k = lenData;
		while (j <= k) {
			for (int l = 0; l < lenData; l++) {
				try {
					int a = data[l];
					int b = data[l+1];
					if (a > b) {
						data[l] = b;
						data[l+1] = a;
					}
				} catch (Exception e) {
				}
			}
			j++;
		}
		System.out.println("SORTED");
		for (int m = 0; m < lenData; m++) {
			System.out.println(data[m]);
		}
	}
}
