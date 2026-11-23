import java.util.Scanner;

public class Fasculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== PRISCULATOR ===");
        System.out.println("counts your prisms");
        System.out.println();

        // INPUT jumlah simpul
        System.out.print("Number of base vertices: ");
        int n = input.nextInt();

        double[] x = new double[n];
        double[] y = new double[n];

        // INPUT koordinat simpulnya (biasanya AB BC CA)
        for (int i = 0; i < n; i++) {
            System.out.print("x" + (i + 1) + ": ");
            x[i] = input.nextDouble();
            System.out.print("y" + (i + 1) + ": ");
            y[i] = input.nextDouble();
        }

        // INPUT tinggi prisma
        System.out.print("Height of prism: ");
        double height = input.nextDouble();

        // ================= LUAS =================
        double areaBaseDouble = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            areaBaseDouble += (x[i] * y[j]) - (y[i] * x[j]);
        }
        areaBaseDouble = Math.abs(areaBaseDouble) / 2.0;
        int areaBaseInt = (int) areaBaseDouble;

        // ================= KELILING =================
        double perimeter = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            double dx = x[j] - x[i];
            double dy = y[j] - y[i];
            perimeter += Math.sqrt(dx * dx + dy * dy);
        }

        // ================= VOLUME =================
        double volumeDouble = areaBaseDouble * height;
        int volumeInt = (int) volumeDouble;

        // ================= OUTPUT =================
        System.out.println("\nBase Area (double) = " + areaBaseDouble);
        System.out.println("Base Area (int) = " + areaBaseInt);
        System.out.println("Perimeter = " + perimeter);
        System.out.println("Volume (double) = " + volumeDouble);
        System.out.println("Volume (int) = " + volumeInt);


    }
}
