package src.lock;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;

class HoldThread implements Runnable{
    private  String locka;
    private  String lockb;

    @Override
    public void run() {
        synchronized (locka){
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println(Thread.currentThread().getName() + " get locka, try get lockb");
            synchronized (lockb){
                try {
                    TimeUnit.SECONDS.sleep(1);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                System.out.println(Thread.currentThread().getName() + " get lockb, try get locka");
            }
        }

    }

    public HoldThread (String locka, String lockb){
        this.locka = locka;
        this.lockb = lockb;


    }
}
public class dead_lock_demo {
    public static void main(String[] args) {
        String locka = "lockA";
        String lockb = "lockB";
        new Thread(new HoldThread(locka,lockb),"new thread name").start();
        new Thread(new HoldThread(lockb,locka),"new thread name").start();

    }
}
