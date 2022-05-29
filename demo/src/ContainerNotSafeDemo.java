import java.util.List;
import java.util.Set;
import java.util.UUID;
import java.util.Vector;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Collections;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.CopyOnWriteArraySet;

public class ContainerNotSafeDemo {
//    static List<String> list = new Vector<>();
    static List<String> list2 = Collections.synchronizedList(new ArrayList<>());
    static List<String> list3 = new CopyOnWriteArrayList<>();
    static Set<String> list = new CopyOnWriteArraySet<String>();
    static HashSet<String> hashSet = new HashSet<String>();
    public  static  void main(String[] args) {
        System.out.println(hashSet);

//        for(int i=1;i<=30;i++){
//            new Thread(()->{
//                list.add(UUID.randomUUID().toString().substring(0,8));
//                System.out.println(list);
//            },String.valueOf(i)).start();
//        }

        for(int i=1;i<=100;i++){
            new Thread(()->{
                hashSet.add(UUID.randomUUID().toString().substring(1,8));
                System.out.println(hashSet);
            },String.valueOf(i)).start();
        }
        //java.util.ConcurrentModificationException

        //解决方法1：vector
        /*
        * 解决方法2： syncchronizeList
        * 解决方法3 ： copyonwritearraylist
        *
        * */

    }
}
