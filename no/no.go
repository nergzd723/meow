package main

import "fmt"
import "os"

func main(){
  arg := os.Args[1:]
  a := arg[0]
  for i := 5; i>0; i++{
    fmt.Println(a)
  }
}
