public class loopWhile {
	public static void main(String [] args) {
		int x, y, z;
		x = 1;
		y = 3;
		while (x <= 4) {
			while (y <= 12) {
				z = x * y;
				System.out.println(x + " x " + y + " = " + z);
				y += 3;
			}
			x += 1;
			y = 3;
		}
	}
}
