package src;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

class MyData{
    volatile int number=0;
    public void addTo60(){
        this.number = 60;
    }
    public  void appPlusPlus(){
        number++;
    }
    AtomicInteger atomicInteger = new AtomicInteger();
    public void addAtomic(){
        atomicInteger.getAndIncrement();
    }
}

/*
* 验证volatile 可见性*/
public class VolatileDemo {
    public static void main(String[] args) {
//        seeOkByVolatile();

        //20个线程操作number++
        MyData myData = new MyData();
        for (int i =1;i<=20 ;i++){
            new Thread(() ->{
                for(int y =1; y<=1000;y++){
                    myData.appPlusPlus();
                    myData.addAtomic();
                }
//                System.out.println(myData.number);
            },String.valueOf(i)).start();
        }
        while (Thread.activeCount()>2){ //说明上面还没有计算完， 最好的控制线程执行时间的方法
            // ，其一是main线程， 2是gc线程
            Thread.yield(); //礼让给别的线程执行，指的是上面的20个线程
            // ,这里很重要， 如果这里20个线程没有执行完， 就不会执行下面的main线程
        };


        System.out.println(Thread.currentThread().getName() +"\t finally number :" + myData.number);
        System.out.println(Thread.currentThread().getName() +"\t finally number :" + myData.atomicInteger);
    }
//volatile 可以保证可见性， 保证主物理内存的变更可以通知到其他线程的工作内存
    private static void seeOkByVolatile() {
        MyData myData = new MyData();
        new Thread(()->{
            System.out.println(Thread.currentThread().getName()+"\t come in");
            try {
                TimeUnit.SECONDS.sleep(3);
                myData.addTo60();
            }
            catch (InterruptedException e){ e.printStackTrace();}
            System.out.println(Thread.currentThread().getName()+
                    "\t updated number value:"+myData.number);

        },"AAA").start();
        while (myData.number ==0){

        }
        ;
        System.out.println(Thread.currentThread().getName()+"\t mission is over" +
                ",main get number value:"+myData.number);
    }
//不保证原子性;某个线程正在做某个业务是， 中间不剋被加塞或者被分割，
// 需要整体完整， 要么同时成功要么同时失败哦



}
