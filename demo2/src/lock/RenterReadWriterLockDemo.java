package src.lock;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class RenterReadWriterLockDemo {
    private volatile  Map<String,Objects> map = new HashMap<>();
    private  ReentrantReadWriteLock reentrantReadWriteLock = new ReentrantReadWriteLock();
    public void   get(String key){
        System.out.println(Thread.currentThread().getName() +"before read");
        map.get(key);
        System.out.println(Thread.currentThread().getName() +"after read");
    }

    public void   put(String key, Objects value){
        System.out.println(Thread.currentThread().getName() +"before write");
        try {
            TimeUnit.SECONDS.sleep(5);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        map.put(key, value);
        System.out.println(Thread.currentThread().getName() +"after write");

    }
    // 解决方案

    public void   get2(String key){
        reentrantReadWriteLock.readLock().lock();
        try{
            System.out.println(Thread.currentThread().getName() +"before read");
//            try {
//                TimeUnit.SECONDS.sleep(200);
//            } catch (InterruptedException e) {
//                e.printStackTrace();
//            }
            map.get(key);
            System.out.println(Thread.currentThread().getName() +"after read");
        }finally {
        reentrantReadWriteLock.readLock().unlock();

    }}

    public void   put2(String key, Objects value){
            reentrantReadWriteLock.writeLock().lock();
            try{
                System.out.println(Thread.currentThread().getName() +"before writer");
                try {
                    TimeUnit.SECONDS.sleep(5);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                map.put(key, value);
                System.out.println(Thread.currentThread().getName() +"after writer");
            }finally {
                reentrantReadWriteLock.writeLock().unlock();

            }}


    public static void main(String[] args) {
        RenterReadWriterLockDemo renterReadWriterLockDemo = new RenterReadWriterLockDemo();
        new Thread(()->{
            renterReadWriterLockDemo.get2("a");

            renterReadWriterLockDemo.put2("a",null);

        },"t1").start();


        new Thread(()->{
            renterReadWriterLockDemo.get2("a");
            renterReadWriterLockDemo.put2("a",null);

        },"t2").start();
    }
    /*
    * 出现t1线程写操作没有遵守原子性
    *
    * 注意点 : map volatile 保证可见性
    * */
}
