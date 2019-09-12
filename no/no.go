package main

import "fmt"
import "os"

func main(){
  arg := os.Args[1:]
  a := arg[0]
  var i int = 0
  for i < 50{
    fmt.Println(a)
  }
}
