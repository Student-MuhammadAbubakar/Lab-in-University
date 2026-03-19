public class Lab7 {
    public static void main(String[] args) {
       /*
        System.out.println("===============Question 1===========");
       String str1="greek";
        String str2="Greek";
       
        if(str1.equals(str2)){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }  \ 
       System.out.println("===============Question 2===========");
       String str="Greeks for greeks" ;
       String replace=str.replace("g","G");
       System.out.println(replace);*/  
         System.out.println("===============Question 3===========");
         String str="Geeksforgeeks" ;
         char[] arr=str.toCharArray();
         for(int i=0;i<arr.length-1;i+=2){
                char temp=arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
}
         System.out.println(new String(arr));
        }
    }