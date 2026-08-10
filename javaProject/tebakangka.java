package javaProject;
import java.util.Scanner;
import java.util.Random;

public class tebakangka {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int angka;
        System.out.println("Game Tebak angka 1-10");
        System.out.println("");

        while (true) {
         System.out.print("Masukkan angka tebakan: ");
        
         angka = scanner.nextInt();
         int angkabenarnya = angkarandom();

         if (angka == angkabenarnya){
             System.out.println("Angka anda benar");
             scanner.close();
             break;
         }else{
             System.out.println("Angka anda salah");
             System.out.println("");
         }
        }
        
        System.out.println("Selesai");
    }
    public static int angkarandom(){
        Random random = new Random();
        int angkabenar = random.nextInt(11);
        
        return angkabenar;

    }
}
