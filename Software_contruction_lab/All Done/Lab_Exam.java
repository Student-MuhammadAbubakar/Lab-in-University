//Question 1: Write a java program for following System



// public class Lab_Exam {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         System.out.print("Enter marks for 5 subjects: ");
//         int sub1 = scanner.nextInt();
//         int sub2 = scanner.nextInt();
//         int sub3 = scanner.nextInt();
//         int subt4 = scanner.nextInt();
//         int sub5 = scanner.nextInt();

//         int total = sub1 + sub2 + sub3 + sub4 + sub5;
//         double percentage = (total / 500.0) * 100;

//         char grade;
//         if (percentage >= 90) {
//             grade = 'A';
//         } else if (percentage >= 80) {
//             grade = 'B';
//         } else if (percentage >= 70) {
//             grade = 'C';
//         } else if (percentage >= 60) {
//             grade = 'D';
//         } else if (percentage >= 40) {
//             grade = 'E';
//         } else {
//             grade = 'F';
//         }

//         System.out.println("Percentage: " + percentage);
//         System.out.println("Grade: " + grade);

//         scanner.close();
//     }
// }





public class Lab_Exam {
//Qusetion 2: Write a java program to find maximum three numbers from the given array of integers without using min and max functions
    public static void main(String[] args) {
        int[] numb = {1, 2, 3, 4, 5, 6, 7};
        int maxi1 = Integer.MIN_VALUE;
        int maxi2 = Integer.MIN_VALUE;
        int maxi3 = Integer.MIN_VALUE;

        for (int num : numb) {
            if (num > maxi1) {
                maxi3 = maxi2;
                maxi2 = maxi1;
                maxi1 = num;
            } else if (num > maxi2 && num != maxi1) {
                maxi3 = maxi2;
                maxi2 = num;
            } else if (num > maxi3 && num != maxi1 && num != maxi2) {
                maxi3 = num;
            }
        }

        System.out.println("The three largest numbers are: " + maxi1 + ", " + maxi2 + ", " + maxi3);
    }
}














// //Question 3: write a java program to swap to numbers
// public class Lab_Exam {
//     public static void main(String[] args) {
//         int a = 6;
//         int b = 7;

//         System.out.println("Before swapping the following: a = " + a + ", b = " + b);
//         int temp = a;
//         a = b;
//         b = temp;

//         System.out.println("After swapping: a = " + a + ", b = " + b);
//     }
// }