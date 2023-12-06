package main

import (
	"bufio"
	. "fmt"
	"os"
)

func main() {
	file, err := os.Open("test.txt")
	if err == nil {
		scannerFile := bufio.NewScanner(file)
	}
	_ = file
	//file,nil := os.Open("input.txt")
}
