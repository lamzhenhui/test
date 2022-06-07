package src.brokenqueue;

import java.util.concurrent.SynchronousQueue;
import java.util.concurrent.TimeUnit;

public class SynchronousQueueDemo {
    public static void main(String[] args) {
        SynchronousQueue<Integer> synchronousQueue = new SynchronousQueue<>();
        new Thread(() ->{
            try {
                System.out.println(Thread.currentThread().getName() + "    put 1");
                synchronousQueue.put(1);
                System.out.println(Thread.currentThread().getName() + "    put 2");
                synchronousQueue.put(2);
                System.out.println(Thread.currentThread().getName() + "    put 3");
                synchronousQueue.put(3);


            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        },"t1").start();

        new Thread(() ->{
            try {
                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                System.out.println(Thread.currentThread().getName() + "    take 1");
                synchronousQueue.take();
                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                System.out.println(Thread.currentThread().getName() + "    take 2");
                synchronousQueue.take();
                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                System.out.println(Thread.currentThread().getName() + "    take 3");
                synchronousQueue.take();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        },"t2").start();


    }
}
