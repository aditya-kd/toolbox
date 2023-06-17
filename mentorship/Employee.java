import java.util.Scanner;
class Employee{

    int en;
    String ename;
    int age;

    Employee(int e, String n, int a){
        en = e;
        ename = n;
        age = a;
    }

    void accept(){
        Scanner sc = new Scanner(System.in);
        int e = sc.nextInt();
        String n = sc.nextLine();
        int ag = sc.nextInt();

        en = e;
        ename = n;
        age = ag;

        sc.close();
    }
    void calculate(){
        System.out.println(en);
        System.out.println(ename);
        System.out.println(age);
    }
    void main(){
        accept();
        calculate();
    }
}