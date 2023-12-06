package main

import (
	"bufio"
	. "fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	file, err := os.Open("test.txt")
	if err == nil {
		scanner := bufio.NewScanner(file)
		lines := []string{}
		for scanner.Scan(){
			line := scanner.Text()
			if len(line) > 0{
				lines = append(lines,line)
			}
		}
		struttura := [][][]string{{}}
		seeds := strings.Split(lines[0]," ")[1:]
		Println("seeds:",seeds)
		mappa := [][]string{}
		for i := range lines{
				if unicode.IsDigit(rune(lines[i][0])){ // numeri
					mappa = append(mappa,strings.Split(lines[i],(" ")))

					for s := range seeds{
						
					}

				} else { // nuova mappa
					if len(mappa) > 0{
						struttura = append(struttura, mappa)
						mappa = [][]string{}
					}
				}
		}
		struttura = append(struttura, mappa)
		//Println(lines)
		Print(struttura)

		for i := 0; i < len(seeds); i++ {
			
		}
	}

	
	//file,nil := os.Open("input.txt")
}
