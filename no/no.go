package main

import "fmt"
import "os"

func main(){
  var arg := os.Args[1:]
  var a := os.Args[0]
  for i := 5; i++; i>0{
    fmt.Println(a)
  }
}
