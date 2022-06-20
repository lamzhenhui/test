package src.thread_pool;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class thread_pool_demo {

    public static void main(String[] args) {
       ExecutorService thread_pool1 = Executors.newFixedThreadPool(3);
       ExecutorService thread_pool2 = Executors.newSingleThreadExecutor();
       ExecutorService thread_pool3 = Executors.newCachedThreadPool();

       try{
           for(int i=1;i<=10; i++){
               thread_pool3.execute(()->{
                   System.out.println(Thread.currentThread().getName() + " 任务执行");
               });
               try {
                       TimeUnit.MILLISECONDS.sleep(200);
               } catch (InterruptedException e) {
                   throw new RuntimeException(e);
               }
           }

       }catch (Exception  e){
           e.printStackTrace();

        }finally {
           thread_pool3.shutdown();
       }
        System.out.println(Runtime.getRuntime().availableProcessors());


    }

}
