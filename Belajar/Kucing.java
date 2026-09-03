package Belajar;

class kucing {

    String nama;
    kucing(){
    }
    kucing(String nama){
        this.nama = nama;
    }
    void mengeong(){
        System.out.println(nama +" ror");
    }
    
}

class kain{
    public static void main(String[] args){
        kucing kucing = new kucing("GalaxyDestroyerWorldEnder");
        kucing.mengeong();
        
    }
}
