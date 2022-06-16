package src.thread_pool;

import java.util.concurrent.*;

public class MyThreadPoolDemo {
    public static void main(String[] args) {
        int corePoolSize =2;
        int maximumPoolSize =5;
        long keepAliveTime=2;
        TimeUnit unit=TimeUnit.SECONDS;
        BlockingQueue workQueue =new LinkedBlockingQueue<>(4);
        ExecutorService executorService = new ThreadPoolExecutor(corePoolSize, maximumPoolSize, keepAliveTime, unit, workQueue,
                Executors.defaultThreadFactory(), new ThreadPoolExecutor.CallerRunsPolicy());


        try {
            for(int i=0;i<=10;i++){
            executorService.execute(()->{
                System.out.println(Thread.currentThread().getName()+" 执行任务");
            });}
        } catch (Exception e) {
            throw new RuntimeException(e);
        }finally {
            executorService.shutdown();
        }



    }
}
