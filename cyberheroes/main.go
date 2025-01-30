package main

import "fmt"


func balik(word string) (r string) {
	for i := len(word) - 1; i >= 0; i-- {
		r += string(word[i])
	}
	return
}

func main(){
	
	fmt.Println(balik("54321@terceSrepuS"))
	
}
