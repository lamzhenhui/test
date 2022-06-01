package src;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.atomic.AtomicStampedReference;

class User
{
    String userName;
    int age;
    int version;

}

public class AtomicReferenceDemo {
    static AtomicReference<Integer> atomicReference2 = new AtomicReference<>(100);
    static AtomicStampedReference<Integer> atomicStampedReference =
            new AtomicStampedReference<>(100,1);
    public static void main(String[] args) {
//        //其他类型的引用
//        User z3 = new User();
//        z3.userName = "z3";
//        z3.age = 12;
//        User z4 = new User();
//        z4.userName = "z4";
//        z4.age = 13;
//
//        AtomicReference<User> atomicReference = new AtomicReference<>();
//        atomicReference.set(z3);
//        atomicReference.set(z4);
        //aba问题
        new Thread(() ->{
            atomicReference2.compareAndSet(100,102);
            System.out.println(Thread.currentThread().getName()+atomicReference2.compareAndSet(102,100));
        },"new thread 1").start();

        new Thread(() ->{
            try{
                TimeUnit.SECONDS.sleep(3);
            }catch (
                    InterruptedException e
            ){e.printStackTrace();};
            System.out.println(Thread.currentThread().getName()+atomicReference2.compareAndSet(100,103));

        },"new thread 2").start();
        try{
            TimeUnit.SECONDS.sleep(1);
        }catch (InterruptedException e){
            e.printStackTrace();
        };
        System.out.println("aba问题产生");
        //aba  solution

        new Thread(() ->{
            int stamp = atomicStampedReference.getStamp();
            System.out.println(Thread.currentThread().getName()+"版本号 " +stamp);
            atomicStampedReference.
                    compareAndSet(100,102,
                            atomicStampedReference.getStamp(),
                            atomicStampedReference.getStamp()+1);

            try{
                TimeUnit.SECONDS.sleep(1);
            }catch (InterruptedException e){
                e.printStackTrace();
            };
            atomicStampedReference.
                    compareAndSet(102,100,
                            atomicStampedReference.getStamp(),
                            atomicStampedReference.getStamp()+1);

        },"new thread 3").start();

        new Thread(() ->{
            int stamp = atomicStampedReference.getStamp();
            System.out.println(Thread.currentThread().getName()+"版本号 " +stamp);

            try{
                TimeUnit.SECONDS.sleep(3);
            }catch (InterruptedException e){
                e.printStackTrace();
            };
            System.out.println(Thread.currentThread().getName()+atomicStampedReference.
                    compareAndSet(102,100,
                            atomicStampedReference.getStamp(),
                            atomicStampedReference.getStamp()+1));


        },"new thread 4").start();

        try{
            TimeUnit.SECONDS.sleep(1);
        }catch (InterruptedException e){
            e.printStackTrace();
        };

        System.out.println("aba问题解决");




    }


}
