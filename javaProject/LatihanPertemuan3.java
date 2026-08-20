/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaProject;
//@author Fahcrul goat larper
import java.util.Scanner;

public class LatihanPertemuan3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        //Balok/Kubus
        System.out.println("KALKULATOR VOLUME BANGUN RUANG BALOK/KUBUS");
        
        System.out.print("Masukkan Panjang: ");
        int panjang = scanner.nextInt() ;
        
        System.out.print("Masukkan Lebar: ");
        int lebar = scanner.nextInt() ;
        
        System.out.print("Masukkan Tinggi: ");
        int tinggi = scanner.nextInt() ;
        
        
        System.out.print("Volume bangun: ");       
        System.out.println(panjang * lebar * tinggi);
        System.out.println("Selesai");
        System.out.println("");
        
        
        //limas segitiga
        System.out.println("KALKULATOR VOLUME BANGUN RUANG LIMAS SEGITIGA");
        System.out.print("Masukkan Luas Alas: ");
        int luasAlas = scanner.nextInt() ;
        
        System.out.print("Masukkan Tinggi Limas: ");
        int tinggiLimas = scanner.nextInt() ;
        
        System.out.print("Volume bangun: ");       
        System.out.println(luasAlas * tinggiLimas / 3);
        System.out.println("Selesai");
        System.out.println("");
        
        
        
        //bola
        System.out.println("KALKULATOR VOLUME BANGUN RUANG BOLA");
        System.out.print("Masukkan Jari-jari: ");
        float jariJari = scanner.nextFloat() ;
        
        double phi = 3.14;
        
        System.out.print("Volume bangun: ");       
        System.out.println(jariJari * jariJari * jariJari * phi * 4 / 3);
        System.out.println("Selesai");

        scanner.close();
    }
    
}
