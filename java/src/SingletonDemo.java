public class SingletonDemo {
    private static SingletonDemo instance = null;
    private SingletonDemo(){
        System.out.println(Thread.currentThread().getName()+"\t 我是构造函数");
    }

    public  static  SingletonDemo getInstance(){
        //单机版的单例
//        if(instance ==null){
//            instance = new SingletonDemo();
//        }
//        return instance;

        //// 双端检锁
        if(instance ==null){
             synchronized (SingletonDemo.class){
                 if(instance ==null){
                     instance =    new SingletonDemo();
                 }
             }
        }
        return instance;
        // 注意:  禁止指令重排,需要在类变量前加volatile ;private static volatile SingletonDemo instance = null;
        /*
        * instance = allocate() //分配对象内存空间
        * instance = memory // 设置instance指向分配的内存空间
        * instance(memory) //初始化对象
        * 这里应为指令重排的原因, 导致, 可能单例实例可能已经不是null, 可是还没有初始话完成, 所以拿到的还是一个空指针.
        * */

    }
    public static void main(String[] args) {
//        SingletonDemo singletonDemo = new SingletonDemo();

        //并发多线程后
        for(int i=1;i<=100000;i++){
            new Thread(()->{
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
            },String.valueOf(i)).start();
        }





    }
}
