public  class nestedarray {
	public static void main(String [] args) {
		int [][] data = new int[3][5];
		for (int i=0;i<data.length;i++) {
			for (int j=0;j<data[i].length;j++) {
				data[i][j] = i;
				System.out.print(data[i][j]);
			}
		System.out.println("	next data ");
		}
	}
}
