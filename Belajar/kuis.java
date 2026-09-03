/*Tujuan sistem ini adalah simulasi transaksi digital dengan layanan berupa 
setor tunai, tarik tunai, dan cek saldo

variabel yang digunakan adalah :
- saldo, biayaAdministrasi, Transaksi dengan tipe data long agar bisa input nominal lebih besar dari int
- menu dengan tipe data int untuk input pilihan layanan dengan menggunakan switch case untuk
eksekusi operasi atau kode program*/
package Belajar;
import java.util.Scanner;

public class kuis{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        long saldo = 500000;
        long biayaAdministrasi = 1000;
        
        enum JenisTransaksi {TARIK_TUNAI , SETOR_TUNAI, CEK_SALDO}

        while (true) {
            System.out.println("");
            System.out.println("Menu ATM");
            System.out.println("1. Tarik Tunai");
            System.out.println("2. Setor Tunai");
            System.out.println("3. Cek Saldo");
            System.out.println("4. Exit");

            System.out.print("Masukkan pilihan menu: ");
            int menu = scanner.nextInt();

        

            switch (menu) {
                case 1:
                    System.out.print("Masukkan Nominal Transaksi: Rp");
                    String nominalTransaksi = scanner.next();
                    long Transaksi = Long.parseLong(nominalTransaksi);

                    long nominal1 = Transaksi;
                    
                    if (saldo - nominal1 - biayaAdministrasi >= 0){
                        saldo = saldo - nominal1 - biayaAdministrasi;
                        System.out.println("Saldo terisa: Rp"+ saldo);
                        System.out.println("Saldo ditarik: Rp"+ nominal1);
                        System.out.println("biaya admin: Rp"+ biayaAdministrasi);
                    }

                    if(saldo - nominal1 - biayaAdministrasi < 0){
                        System.out.println("Saldo tidak cukup");
                    }
                    break;
            
                case 2:
                    System.out.print("Masukkan Nominal Transaksi: Rp");
                    String nominalTransaksi1 = scanner.next();
                    long Transaksi1 = Long.parseLong(nominalTransaksi1);
                    Long nominal2 = Transaksi1;
                    saldo = saldo + nominal2;
    
                    System.out.println("Saldo ditambah: Rp"+ nominal2);
                    System.out.println("Saldo total: Rp"+ saldo);

                    break;
            
                case 3:
                    System.out.println("Sisa Saldo anda adalah Rp" + saldo);
                    break;
            
                case 4:
                    System.out.println("Program berhenti...");
                    return;
                    
            }
        } 
    }
}