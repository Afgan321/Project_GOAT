package javaProject;
import java.util.Scanner;

public class clas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        hero clint = new hero();
    
        System.out.print("masukkan Sklll: ");
        clint.skill = scanner.nextLine();

        System.out.print("masukkan damage: ");
        clint.damage = scanner.nextInt();
        System.out.println();

        scanner.close();
        System.out.println(clint.skill);
        System.out.print(clint.damage);
        System.out.println("selesai");
    }

    public static class hero{
        String skill;
        int damage;

        hero(){
        }

        hero(String skill, int damage){
            this.skill = skill;
            this.damage = damage;

        }
    }
    

}
