package main

import (
	"bufio"
	. "fmt"
	"os"
	_ "slices"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	file, _ := os.Open("test.txt")
	//file, err := os.Open("input.txt")
	scanner := bufio.NewScanner(file)

	min := 100000000000000

	scanner.Scan()
	line := scanner.Text()
	cnt :=0
	seedstring := strings.Split(line, " ")[1:]
	//Println(seedstring)
	seed := 0
	for i := 0; i < len(seedstring); i += 2 {
		startSeed, _ := strconv.Atoi(seedstring[i])
		rangee, _ := strconv.Atoi(seedstring[i+1])
		for s := 0; s < rangee; s++ {
			seed = startSeed + s
			Println(" seed", seed)

			//var mappa [][]string
			status := true
			for scanner.Scan() {
				line := scanner.Text()
				if len(line) > 0 && status{
					if unicode.IsDigit(rune(line[0])) && status { // numeri
						//mappa = append(mappa, strings.Split(line, (" ")))
						numbers := strings.Split(line, (" "))

						//Println("m", numbers)
						//var history []int
						dest, _ := strconv.Atoi(string(numbers[0]))
						source, _ := strconv.Atoi(string(numbers[1]))
						rangeee, _ := strconv.Atoi(string(numbers[2]))

						if seed >= source && seed < source+rangeee /*&& slices.Index(history, s) == -1*/ {
							diff := seed - source
							seed = (dest + diff)
							
							status = false
							//history = append(history, seed)
						}

					} else {
						status = true
					}
					Print(status,"")
				}
			}

			// Println("New Scan")
			scanner = bufio.NewScanner(file)
			
			cnt+=1
			Print(min,seed,seed<min)
			if seed < min {
				min = seed
				Println("min=", seed)
	
			}
		}

	}
	Println()

	//Println("minimo:", min)

}
