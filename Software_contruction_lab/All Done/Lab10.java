public class Lab10{
    static void welcomeMessage(){
        System.out.println("Welcome to Java");
    }
    static int newmethod(int x,int y){
        return x+y;
    }
    static double newmethodplus(double x,double y){
        return x+y;
    }
    public static void main(String[] args) {
        welcomeMessage();
        int num1 = newmethod(3, 10);
        System.out.println("Number is " + num1);
        double num2 = newmethodplus(5.5, 10.5);
        System.out.println("Number is " + num2);
    }
}