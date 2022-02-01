//Zach Hower
//2022-01-31
//Lab3 Part1

import java.util.Scanner;

public class Lab3_Part1 {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter a whole number: ");
            int num1 = input.nextInt();

            System.out.print("Enter a whole number: ");
            int num2 = input.nextInt();

            System.out.print("Enter a whole number: ");
            int num3 = input.nextInt();

            System.out.print("Enter a whole number: ");
            int num4 = input.nextInt();

            System.out.print("Enter a whole number: ");
            int num5 = input.nextInt();

            int numMax1 = Math.max(num1, num2);
            int numMax2 = Math.max(num3, num4);
            int numMax3 = Math.max(numMax1, numMax2);
            int numMax4 = Math.max(numMax3, num5);

            int numMin1 = Math.min(num1, num2);
            int numMin2 = Math.min(num3, num4);
            int numMin3 = Math.min(numMin1, numMin2);
            int numMin4 = Math.min(numMin3, num5);

            System.out.printf("The maximum number is: %d%n", numMax4);
            System.out.printf("The minimum number is: %d", numMin4);
        }

    } // end method
} // end class
