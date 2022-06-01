package src;

import java.util.concurrent.atomic.AtomicInteger;

public class CasDemo {

    public static void main(String[] args) {
        AtomicInteger atomicInteger = new AtomicInteger(5);
        atomicInteger.compareAndSet(5,10);

        System.out.println(atomicInteger);
        atomicInteger.getAndIncrement();

    }
}
