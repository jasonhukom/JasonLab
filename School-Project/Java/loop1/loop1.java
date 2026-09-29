import java.util.Scanner;

public class loop1 {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		boolean again;
		char answer;

		do {
			System.out.println("Loop how many times?");
			int loop = input.nextInt();

			System.out.println();

			for (int i = 1; i <= loop; i++) {
				for (int j = 1; j <= i; j++) {
					System.out.print("1");
				}
				System.out.println("");
			}

			System.out.println("Again? (Y/n)");
			answer = input.next().charAt(0);
			if (Character.toUpperCase(answer) == 'Y') {
				again = true;
			} else {
				again = false;
			}
		} while (again == true);
	}
}
