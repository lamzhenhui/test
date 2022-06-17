package src.thread_pool;

import java.util.concurrent.*;

public class MyThreadPoolDemo {
    public static void main(String[] args) {
        int corePoolSize =2;
        int maximumPoolSize =5;
        long keepAliveTime=1;
        TimeUnit unit=TimeUnit.MILLISECONDS;
        BlockingQueue workQueue =new LinkedBlockingQueue<>(2);
        ExecutorService executorService = new ThreadPoolExecutor(corePoolSize, maximumPoolSize, keepAliveTime, unit, workQueue,
                Executors.defaultThreadFactory(), new ThreadPoolExecutor.CallerRunsPolicy());


        try {
            for(int i=1;i<=12;i++){
            executorService.execute(()->{
                System.out.println(Thread.currentThread().getName()+" 执行任务");
            });}
        } catch (Exception e) {
            e.printStackTrace();
        }finally {
            executorService.shutdown();
        }



    }
}
