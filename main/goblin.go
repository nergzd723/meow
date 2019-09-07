package main
import(
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
func main(){
	rand.Seed(time.Now().UnixNano())
	fmt.Println(rand.Intn(100))
	for i:=0; i<50000000; i++{
		var n int = (rand.Intn(10000000))
		f := float64(n)
		domath(f)
	}

}
