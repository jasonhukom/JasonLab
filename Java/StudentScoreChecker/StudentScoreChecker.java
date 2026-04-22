import java.util.Scanner;
import java.util.Arrays;

public class StudentScoreChecker {
	public static void main(String [] args) {
		Scanner input = new Scanner(System.in);
		int x, i, j, k; // Iteration Helper

		String name;
		int amountOfStudents, amountOfSubjects;
		int[][] score; // [score] [amountOfSubjects]

		System.out.print("How many student are there? ");
		amountOfStudents = input.nextInt();
		System.out.print("How many subjects are there? (Rec: 5) ");
		amountOfSubjects = input.nextInt();

		score = new int[amountOfSubjects][amountOfStudents];
		String[] studentsName = new int[amountOfStudents];

		System.out.println();
		System.out.println("     -~~===+ Subjects +===~~-");
		for (x = 0; x < amountOfSubjects; x++) {
			System.out.println("");
		}
		System.out.println();
		// i = Students
		for (i = 0; i < amountOfStudents; i++) {
			System.out.print("Name: ");
			studentsName[i] = input.nextLine();
			for (int j = 0; j < amountOfSubjects) {
				
			}
		}
	}
}
