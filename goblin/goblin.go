package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func domath(number uint64) {
	var d = number * number * number * number * number
	var id = d * d * d * d * d
	id++
	fmt.Println(d, id)
	
}
func main() {
	start := time.Now()
	rand.Seed(time.Now().UnixNano())
	var n int
	for i := 0; i < 5000000; i++ {
		n = rand.Intn(10000000)
		f := uint64(n)
		domath(f)
	}
	elapsed := time.Since(start)
	fmt.Println(elapsed)

}
