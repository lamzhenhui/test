package src.brokenqueue;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

class ShardData{
    private  AtomicInteger number = new AtomicInteger();
    private volatile  boolean flag = true;
    private BlockingQueue<String> blockingQueue = null;
    public  ShardData(BlockingQueue<String> blockingQueue){
        this.blockingQueue = blockingQueue;
        System.out.println(this.blockingQueue.getClass().getName());

    }
    public void  my_prod(BlockingQueue blockingQueue){
        boolean return_value;
        String data;
        while(flag){
            data = number.getAndIncrement()+""; // 这里应该用引用，
            try {
                return_value = blockingQueue.offer(data,2,TimeUnit.SECONDS);
                if (return_value){
                    System.out.println("插入队列" + data + "成功");
                }else {
                    System.out.println("插入队列" + data + "失败");
                }
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
        System.out.println("老板喊停, 停止生产");
    }

    public void  my_consumer() throws Exception{
        String return_value = null;
        while(flag){
            try {
                return_value = (String) blockingQueue.poll(2,TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            if (return_value == null || "".equalsIgnoreCase(return_value)){
                flag=false;
                System.out.println("查询2秒仍然无法获取数据, 消费停止");
                return ;
            }else {
                System.out.println("查询队列" + return_value + "成功");
            }
        }
    }

    public void set_stop(){
        flag = false;
    }

}
public class ProdConsumerBlockQueueDemo {
    public static void main(String[] args) {
        BlockingQueue<String> blockingQueue = new ArrayBlockingQueue<>(10);
        ShardData shardData = new ShardData(blockingQueue);
        new Thread(() ->{
            shardData.my_prod(blockingQueue);
        },"aa ").start();


        new Thread(() ->{
            try {
                shardData.my_consumer();
//                TimeUnit.SECONDS.sleep(1);
            } catch (Exception e) {
                e.printStackTrace();
            }
        },"bb ").start();

        try {
            TimeUnit.SECONDS.sleep(5);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("5秒后老板喊停");
        shardData.set_stop();


    }


}
