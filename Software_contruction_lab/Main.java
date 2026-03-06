public class Main {
    public static void main(String[] args) {
        int y = 100;
        int x = 90;
        int z = 94;
        int sum = x + y + z;
        double average = (double)(x+y+z) / 3.0;
        System.out.printf("The Sum of the %d, %d and %d is: %d and the average is %s%n and the number of elements is 3", x, y, z, sum, average);
    }
}