package main

import "fmt"

func main() {
	print(123)
	d :=Dog{
		name: "dog1",
	}
	fmt.Printf("dog %s",d)
}
type Dog struct {
	name string
}

func (dog *Dog) SetName(name string) {
	dog.name = name
}
