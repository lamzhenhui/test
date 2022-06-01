package src.lock;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;

public class SpinLockDemo {
    AtomicReference atomicReference = new AtomicReference();
    public void lock(){
        Thread thread = Thread.currentThread();
        while (!atomicReference.compareAndSet(null,thread)){

        }
        System.out.println("invoked src.lock");


    };
    public void unlock(){
        Thread thread = Thread.currentThread();
        while (!atomicReference.compareAndSet(thread,null)){

        }
        System.out.println("invoked unlock");


    };

    public static void main(String[] args) {
        SpinLockDemo spinLockDemo = new SpinLockDemo();

        new Thread(()->{
            spinLockDemo.lock();

            try {
                TimeUnit.SECONDS.sleep(5);

            } catch (InterruptedException e) {
                e.printStackTrace();
            }


            spinLockDemo.unlock();

        },"t1").start();

        new Thread(()->{
            spinLockDemo.lock();

            spinLockDemo.unlock();

        },"t2").start();


    }
}
