package lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.TimeUnit;

class Phone{
    public synchronized void sentSms()throws Exception{
        System.out.println(Thread.currentThread().getName() + "run sms");
        sentEmail();
    };

    public synchronized void sentEmail()throws Exception{
        System.out.println(Thread.currentThread().getName() + "run email");
    };
}

class Phone2 implements Runnable{
    private Lock lock = new ReentrantLock();
    public  void  get() {
        lock.lock();
        System.out.println(Thread.currentThread().getName() +"get run");
        set();
        lock.unlock();
    }

    public  void  set() {
        lock.lock();
        System.out.println(Thread.currentThread().getName() +"set run");
        lock.unlock();
    }
    @Override
    public void run(){
        get();

    }


}

public class ReenterLockDemo {
    public static void main(String[] args) {
        Phone phone = new Phone();
        Phone2 phone2 = new Phone2();

        new Thread(()->{
            try {
                phone.sentSms();
            } catch (Exception e) {
                e.printStackTrace();
            }
        },"thread name t1").start();

        new Thread(()->{
            try {
                phone.sentSms();
            } catch (Exception e) {
                e.printStackTrace();
            }
        },"thread name t2").start();
        System.out.println();
        System.out.println();
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println();

        System.out.println();
        new Thread(()->{
            try {
                phone2.get();
            } catch (Exception e) {
                e.printStackTrace();
            }
        },"thread name t3").start();

        System.out.println();
        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println();

        Thread t4 = new Thread(phone2);
        t4.start();


    }
}
