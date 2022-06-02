package src.CountDownLatch;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.TimeUnit;


// enum CountryEnum{
//     COUNTRY_ENUM(Integer code, String name){
//
//     }
//
//}

public class CountDownLatchDemo {
    private static  CountDownLatch countDownLatch = new CountDownLatch(4);
    private static  CyclicBarrier cyclicBarrier = new CyclicBarrier(4,()->{
        System.out.println("可以锁门");

    //使用枚举

    });
    public static void main(String[] args) {
        for(int i=1;i<=4;i++){
            new Thread(()->{
                System.out.println("第" + Thread.currentThread().getName() + "位同学离开教室");
                countDownLatch.countDown();
            },String.valueOf(i)).start();
        }
        try {
            countDownLatch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("班长锁门");

        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        for(int i=1;i<=4;i++){
            new Thread(()->{
                System.out.println("第" + Thread.currentThread().getName() + "位同学离开教室");


                try {
                    cyclicBarrier.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (BrokenBarrierException e) {
                    e.printStackTrace();
                }
            },CountryEnum.forEach(i).getValue()).start();
        }
//        System.out.println("班长可以锁门");
    }
}
