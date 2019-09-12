// Infinite forking
// Test your RAM!
// by nergzd723
package main
func main(){
  for{
    go main()
  }
}
