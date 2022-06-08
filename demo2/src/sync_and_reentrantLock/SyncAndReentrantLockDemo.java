package src.sync_and_reentrantLock;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;

class ShardData{
    private int mub = 1;
    private Lock lock = new ReentrantLock();
    private Condition c1 = lock.newCondition();
    private Condition c2 = lock.newCondition();
    private Condition c3 = lock.newCondition();
    public void print5(){
        lock.lock();
        try {
            while (mub !=1){
                c1.await();
            }
            System.out.println(Thread.currentThread().getName() + "打印5");
            mub=2;
            c2.signal();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            lock.unlock();
        }
    }

    public void print10(){
        lock.lock();
        try {
            while (mub !=2){
                c2.await();
            }
            System.out.println(Thread.currentThread().getName() + "打印10");
            mub =3;
            c3.signal();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            lock.unlock();
        }
    }
    public void print100(){
        lock.lock();
        try {
            while (mub !=3){
                c3.await();
            }
            System.out.println(Thread.currentThread().getName() + "打印100");
            mub =1;
            c1.signal();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            lock.unlock();
        }
    }

}
public class SyncAndReentrantLockDemo {
    public static void main(String[] args) {
        ShardData shardData = new ShardData();
        new Thread(() ->{
            for(int i=1;i<=10;i++){
            shardData.print5();

            }
        },"aa ").start();

        new Thread(() ->{
            for(int i=1;i<=10;i++){
                shardData.print10();

            }
        },"bb ").start();

        new Thread(() ->{
            for(int i=1;i<=10;i++){
                shardData.print100();

            }
        },"cc ").start();


    }

}
