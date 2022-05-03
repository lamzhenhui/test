/*
* 指令重排序案例*/

public class ResourceSeqDemo {
     int a = 0;
     boolean flag = false;

    public void method01() {
        a = 1;
        flag = true;
//        System.out.println("rev");
    }

    public void method02() {
        if (flag) {
            a = a+5;
            System.out.println("***retValue" + a);
        }
    }

    public static void main(String[] args) {
        for (int i=0; i<=2000;i++){
            ResourceSeqDemo resourceSeqDemo = new ResourceSeqDemo();
            new Thread(() ->{
                resourceSeqDemo.method01();
                resourceSeqDemo.method02();
            },"aaa").start();
        }
    }

}
