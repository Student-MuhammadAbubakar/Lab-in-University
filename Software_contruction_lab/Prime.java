
public class Prime {
    public static void main(String[] args) {
        int n=100;
        for(int i=2;i<=n;i++){
            int j;
            for(j=2;j<i;j++)
                if(i%j==0){
                    break;
                }
                if(j==i){
                    System.out.println(i);
                }
            
        }
    }
}
