import java.util.Scanner;



public class studi {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        
        
        String word;

        word = scanner.next();
        hitungvokalkonsonan(word);
        scanner.close();
        System.out.println("selesai");
    }
        
    public static void hitungvokalkonsonan(String word){
        int i;
        int jumlahvokal = 0;
        int jumlahkonsonan = 0;

        for (i = 0; i < word.length(); i++){
            if (word.charAt(i) == 'a' || word.charAt(i) == 'i' || word.charAt(i) == 'u' || word.charAt(i) == 'e' || word.charAt(i) == 'o'){
                jumlahvokal++;


            } else{
                jumlahkonsonan++;
            }
        }
        System.out.println("jumlah vokal= "+ jumlahvokal+"jumlah konsonan= "+ jumlahkonsonan);
    } 
    
}