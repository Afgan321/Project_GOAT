package javaProject;

public class clas {
    public static void main(String[] args) {
        hero clint = new hero();
    
        clint.skill = "tembak";


        System.out.println(clint.skill);
        System.out.println("selesai");
    }

    public static class hero{
        String skill;
        int damage;

        hero(){
        }

        hero(String skill){
            this.skill = skill;

        }
    }
    

}
