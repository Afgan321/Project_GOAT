package javaProject;

public class latihan {
    public static void main(String[] args){

        String nama = "Ahmad Fahcrul Siagian";
        long nim = 25071207786L;
        String kelas = "TI-A"; 
        String jurusan = "Teknik Informatika";
        int tinggiBadan = 160;
        boolean mahasiswa = true;

        System.out.println("Nama:           : "+ nama);
        System.out.println("NIm:            : "+ nim);
        System.out.println("Kelas:          : "+ kelas);
        System.out.println("Jurusan         : "+ jurusan);
        System.out.println("Tinggi Badan    : "+ tinggiBadan + " Cm");
        System.out.println("Status Mahasiswa: "+ mahasiswa);
        System.out.println();
        panggilan(nama);
    }

    public static void panggilan(String nama){
        System.out.println("Hallo!!! "+ nama);

    }
}
