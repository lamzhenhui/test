package src.CountDownLatch;

import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

public class SemaphoreDemo {
    public static void main(String[] args) {

        Semaphore semaphore = new Semaphore(3);
        for (int i = 1; i <= 10; i++) {
            new Thread(() -> {
                try {
                    semaphore.acquire();
                    System.out.println(Thread.currentThread().getName() + "抢到车位");
                    try {
                        TimeUnit.SECONDS.sleep(3);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } catch (
                        InterruptedException e
                ) {
                    e.printStackTrace();
                }finally {
                    System.out.println(Thread.currentThread().getName() + "离开车位");
                    semaphore.release();
                }
            }, String.valueOf(i)).start();
        }

    }


}
