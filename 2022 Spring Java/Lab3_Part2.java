//Zach Hower
//2022-01-31
//Lab3 Part1

import java.util.Scanner;

public class Lab3_Part2 { 
    public static void main(String[] args) {

        try (Scanner input = new Scanner(System.in)) { //instantiates a scanner
            //TODO learn how to use try-catch blocks
           
            System.out.print("Enter a whole number: "); // Grabs int from user
            int num = input.nextInt();

            String even = ""; // Initiates even as empty string

            // Determines if num is odd or even and returns to even
            if (num % 2 == 0) {
                even = "Even";
            }
            else {
                even = "Odd";
            }

            System.out.printf("The number is %s", even); // Displays even or odd
        }
    } // end method
} // end class