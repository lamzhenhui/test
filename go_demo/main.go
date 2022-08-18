package main

import (
	"fmt"
)

func main() {
	print(123)
	d := Dog{
		name: "dog1",
	}

	fmt.Printf("dog %s", d)

	ch1 := make(chan int, 3)
	ch1 <- 2
	ch1 <- 1
	ch1 <- 3
	elem1 := <-ch1

	fmt.Printf("The first element received from channel ch1: %v\n",
		elem1)

	elem2 := <-ch1

	fmt.Printf("The first element received from channel ch1: %v\n",
		elem2)

	elem3 := <-ch1

	fmt.Printf("The first element received from channel ch1: %v\n",
		elem3)
	elem4 := <-ch1

	fmt.Printf("The first element received from channel ch1: %v\n",
		elem4)
}

type Dog struct {
	name string
}

func (dog *Dog) SetName(name string) {
	dog.name = name
}
