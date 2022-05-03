public class SingletonDemo {
    private static SingletonDemo instance = null;
    private SingletonDemo(){
        System.out.println(Thread.currentThread().getName()+"\t 我是构造函数");
    }

    public static SingletonDemo getInstance(){
        if(instance ==null){
            instance = new SingletonDemo();
        }
        return instance;
    }
    public static void main(String[] args) {
//        SingletonDemo singletonDemo = new SingletonDemo();

        //并发多线程后
        for(int i=1;i<=10;i++){
            new Thread(()->{
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
                SingletonDemo.getInstance();
            },String.valueOf(i)).start();
        }


    }
}
