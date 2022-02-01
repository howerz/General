//Zach Hower
//2022-01-31
//Lab3 Part1

import java.util.Scanner;

public class Lab3_Part1 { 
    public static void main(String[] args) {
        // VS code suggested I close this with a try? I do not understand why
        try (Scanner input = new Scanner(System.in)) { //instantiates a scanner input
            
            // Grabs 5 ints from user
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

            // using Java.Lang.Math methods
            // I assume this lab is to help learn the fundamentals of operators and if statements
            // and this kind of defeats that purpose.
            // Let me know if you would like me to stick to what the lesson is trying to teach explicitly.
            // For completeness, I know this method does take more momery (2 extra variables)
            // It also may be slightly less efficient (it performs a NaN check and a -0 check first)
            // but I find it much more readable and those cons have a negligible effet for such a small program
            int numMax = Math.max(num1, num2);
            numMax = Math.max(numMax, num3);
            numMax = Math.max(numMax, num4);
            numMax = Math.max(numMax, num5); // Returns max value

            int numMin = Math.min(num1, num2);
            numMin = Math.min(numMin, num3);
            numMin = Math.min(numMin, num4);
            numMin = Math.min(numMin, num5); // Returns min value

            System.out.printf("The maximum number is: %d%n", numMax); // Displays max value
            System.out.printf("The minimum number is: %d", numMin); // Displays min value
        }

    } // end method
} // end class
