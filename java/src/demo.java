public class demo {
    int numb = 0;
    boolean flag = false;
    public void met1(){
        numb= 1;
        flag = true;
    }

    public void met2(){
        if(flag){
            numb +=5;
            System.out.println("print " +numb);
        }
    }

    public static void main(String[] args) {
        demo demo1 = new demo();
        for(int i=0; i<1000;i++){
            demo1.flag=true;
            demo1.met2();
//            System.out.println(1);
        }
    }
}
