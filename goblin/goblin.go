package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func domath(number float64) {
	var d = math.Pow(number, 20)
	var id = math.Pow(d, 20)
	id++
}
func main() {
	start := time.Now()
	rand.Seed(time.Now().UnixNano())
	var n int
	for i := 0; i < 50000000; i++ {
		n = rand.Intn(10000000)
		f := float64(n)
		domath(f)
	}
	elapsed := time.Since(start)
	fmt.Println(elapsed)

}
