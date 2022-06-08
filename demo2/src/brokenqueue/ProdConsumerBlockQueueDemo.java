package src.brokenqueue;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

class ShardData{
    private  AtomicInteger number = new AtomicInteger(1);
    private volatile  boolean flag = true;
    private BlockingQueue blockingQueue = null;
    public void  my_prod(BlockingQueue blockingQueue){
        boolean return_value;
        while(flag){
            String data = number.getAndIncrement()+"";
            try {
                return_value = blockingQueue.offer(data,2,TimeUnit.SECONDS);
                if (return_value){

                    System.out.println("插入队列成功");
                }else {
                    System.out.println("插入队列失败");

                }
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }


        }
        System.out.println("老板喊停, 停止生产");
    }

    public void  my_consumer(){
        String result =null;
        while(flag){
            if (number !=null || "".equalsIgnoreCase(number+"")){}
                try {
                    result = blockingQueue.poll(2,TimeUnit.SECONDS);
                    if (return_value){

                        System.out.println("插入队列成功");
                    }else {
                        System.out.println("插入队列失败");

                    }
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }


        }
        System.out.println("老板喊停, 停止生产");
    }



    public void set_stop(){
        this.flag = false;
    }

}
public class ProdConsumerBlockQueueDemo {
    public static void main(String[] args) {
        ShardData shardData = new ShardData();
        BlockingQueue<String> blockingQueue = new ArrayBlockingQueue<>(3);
        new Thread(() ->{
            shardData.my_prod(blockingQueue);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        },"aa ").start();


        new Thread(() ->{
            shardData.my_consumer(blockingQueue);
        },"bb ").start();

        try {
            TimeUnit.SECONDS.sleep(1);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        shardData.set_stop();
        System.out.println("老板喊停");


    }


}
