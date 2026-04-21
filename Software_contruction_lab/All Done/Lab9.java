public class Lab9{
    public static void main(String[] args){
     String[] cars={"Volvo","BMW","Ford","Mazda"};
     cars[0]="Opel";
     System.out.println(cars[0]);
     System.out.println(cars.length);
     int[] myNum={10,20,30,40};
     for(int i=0;i<myNum.length;i++){
         System.out.println(myNum[i]);
     }
     for(String data:cars){
        System.out.println(data);
     }
     String[] seats={"Ali","Veli","Ayşe"};
     for(int i=0;i<seats.length;i++){
         System.out.println("The seat number "+i+" is for "+seats[i]);
     }
     int[] ages={10,20,30,40};
     int sum=0;
        for(int i=0;i<ages.length;i++){
            sum+=ages[i];
        }
        System.out.println("The sum of ages is "+sum);
        float avg=sum/ages.length;
        System.out.println("The average of ages is "+avg);
        int[][] matrix={{1,2,3,4,5},{4,5,6,7,8},{7,8,9,10,11},{10,11,12,13,14}};
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
       System.out.println(matrix.length+" x "+matrix[0].length);
    }
}