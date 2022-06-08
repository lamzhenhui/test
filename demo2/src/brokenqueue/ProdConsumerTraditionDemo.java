package src.brokenqueue;

import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.Condition;
class SareData{
    private Lock lock = new ReentrantLock();
    private Condition condition = lock.newCondition();

    private int number = 0;
    public void increase(){
        lock.lock();
        try {
            while (number!=0){

                //阻塞 不生产
                condition.await();
            }
            System.out.println(Thread.currentThread().getName() + " 生产一个蛋糕");
            number++;
            condition.signalAll();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            lock.unlock();
        }

    }

    public void decrease(){
        lock.lock();
        try {
            while (number==0){

                //阻塞 不生产
                condition.await();
            }
            System.out.println(Thread.currentThread().getName() + " 消费一个蛋糕");
            number--;
            condition.signalAll();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            lock.unlock();
        }

    }
}

public class ProdConsumerTraditionDemo {
    /*
    * 1 多线程操作资源类
    * 2 判断 干活 通知唤醒
    * 3 预防虚假唤醒 通过用while解决多线程下导致的虚假唤醒和中断问题*/
    public static void main(String[] args) {
        SareData sareData = new SareData();
        for(int i=1;i<=10;i++){
            new Thread(()->{
                try {
                    sareData.increase();
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
//                sareData.decrease();
            },"aa").start();
        }

        for(int i=1;i<=10;i++){
            new Thread(()->{
//                sareData.increase();
                try {
                    sareData.decrease();
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            },"bb").start();
        }
        for(int i=1;i<=10;i++){
            new Thread(()->{
//                sareData.increase();
                try {
                    sareData.decrease();
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            },"cc").start();
        }
        for(int i=1;i<=10;i++){
            new Thread(()->{
//                sareData.increase();
                try {
                    sareData.decrease();
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            },"dd").start();
        }

    }
}
