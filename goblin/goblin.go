package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func domath(number float64) {
	var d = math.Pow(number, 15)
	var id = math.Pow(d, 15)
	id++
	fmt.Println(d, id)
	
}
func main() {
	start := time.Now()
	rand.Seed(time.Now().UnixNano())
	var n int
	for i := 0; i < 5000000; i++ {
		n = rand.Intn(10000000)
		f := float64(n)
		domath(f)
	}
	elapsed := time.Since(start)
	fmt.Println(elapsed)

}
