import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.IOException;
import java.util.List;

public class buffread{
    public static void main(String[] args){



        InputStreamReader inputStreamReader = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(inputStreamReader);


        try {
            System.out.print("Masukkan Angka: ");
            int angka = Integer.parseInt(br.readLine());

            System.out.print("Masukkan kata: ");
            String kata = br.readLine();

            System.out.println("ini ouputnya " + angka +" " +kata);

        } catch (IOException e){
            System.out.println("error");
        }

        perulangan p = new perulangan();
        p.hebat();

        System.out.println("selesai");
    }
}



class perulangan {
    void hebat(){
        List<String> gw = new ArrayList<>();

        gw.add("sigma");
        gw.add("ganteng");

        for (int i = 0; i < gw.size(); i++){

            System.out.println(i+1 +". "+gw.get(i));
        }



    }





}