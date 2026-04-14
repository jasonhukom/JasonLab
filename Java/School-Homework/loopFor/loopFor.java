public class loopFor {
	public static void main(String [] args) {
		int k;
		for (int i = 1; i <= 4; i++) {
			for (int j = 12; j >= 3; j -= 3) {
				k = i * j;
				System.out.println(i + " x " + j + " = " + k);
			}
		}
	}
}
