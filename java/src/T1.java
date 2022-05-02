public class T1 {
    volatile int num =1;
    public void addNum(){
        num++;
    }

    public static void main(String[] args) {
        T1 t1 = new T1();
        t1.addNum();
    }
}
