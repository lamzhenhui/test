class People{
    int age;
    String name;
    public People(String name){
        this.name =name;
    };

    public void setName(String name) {
        this.name = name;
    }
}

public class TransferValueDemo {
    private static TransferValueDemo transferValueDemo;

    public void ChangeValue1(int age){
        age = 30;
    };
    public void ChangeValue2(People people){
        people.setName("xxx");
    };
    public void ChangeValue3(String str){
        str = "z4" ;
    };
    public static void main(String[] args) {
        TransferValueDemo transferValueDemo = transferValueDemo;
        int age = 13;
        transferValueDemo.ChangeValue1(age);
        System.out.println("age" + age);

        People people = new People("l4");
        transferValueDemo.ChangeValue2(people);
        System.out.println("name" + people.name);

        String str = "next";
        transferValueDemo.ChangeValue3(str);
        System.out.println("str" + str);







    }

}
