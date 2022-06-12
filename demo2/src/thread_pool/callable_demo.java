package src.thread_pool;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;
import java.util.concurrent.TimeUnit;

class MyThread implements Callable{
    @Override
    public Object call() throws Exception {
        TimeUnit.SECONDS.sleep(5);
        System.out.println("callable start");
        System.out.println("callable 线程执行用时5秒钟 并拿到结果result2 =" + 1024);
        return 1024;
    }
}
public class callable_demo {
    public static void main(String[] args) {
        int result2=0;
        int result1=100;
        MyThread myThread = new MyThread();
        FutureTask<Integer> futureTask = new FutureTask<>(myThread);
        Thread thread = new Thread(futureTask,"aaa");
        thread.start();
        try {
            TimeUnit.SECONDS.sleep(2);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("*******main线程执行了两秒钟并拿到结果result1 =" + result1);
//        while (!futureTask.isDone()){
//
//        }
        try {
            result2 = futureTask.get();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
//        System.out.println(thread.getName());
        System.out.println("返回结果"+(result2 +result1));
//        thread.getName();
    }
}
