import java.util.Scanner;

public class HelloWorld{
    public static void main(String[] args){
        System.out.println("hebat");

        char []  makanan = {'a', 'y', 'a', 'm'} ;
        System.out.println(makanan) ;

        String jane = "hebat";
        int panjang = jane.length();
        System.out.println(panjang);

        char gw = jane.charAt(1);
        System.out.println(gw);

        int hasilhitunggw = 5 * 6 ;
        System.out.println(hasilhitunggw);

        int a = 5;
        int b = 6;
        boolean benar;
        benar = a == b;
        System.out.println("5 = 6 mah " + benar);

        int c = 7;
        int d = 8;
        boolean result = d == 10 && c == 7 ;
        boolean anotherresult = d == 10 || c == 7;
        System.out.println(result);
        System.out.println(anotherresult);

        Scanner scanner = new Scanner(System.in);
        int angka = scanner.nextInt();
        System.out.println(angka);
        scanner.close();




    }


}