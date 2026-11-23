import java.util.Scanner;
import java.util.Arrays;

public class NestedArrayInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Define dimensions
        System.out.print("Enter number of rows: ");
        int rows = sc.nextInt();
        System.out.print("Enter number of columns: ");
        int cols = sc.nextInt();

        int[][] matrix = new int[rows][cols];

        // Fill nested array
        System.out.println("Enter array elements:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
	System.out.println(Arrays.deepToString(matrix));
        sc.close(); // Recommended best practice
    }
}
