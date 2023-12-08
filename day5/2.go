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
	//file, _ := os.Open("test.txt")
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	min := 100000000000000

	scanner.Scan()
	line := scanner.Text()
	seedstring := strings.Split(line, " ")[1:]
	var maps []string
	for scanner.Scan(){
		maps = append(maps,scanner.Text())
	}
	file.Close()
	
	seed := 0	
	for i := 0; i < len(seedstring); i += 2 {
		startSeed, _ := strconv.Atoi(seedstring[i])
		rangee, _ := strconv.Atoi(seedstring[i+1])
		for s := 0; s < rangee; s++ {
			seed = startSeed + s
			Println(i,"/",len(seedstring)/2,"\t",seed)
			status := true

			for j := range maps {
				line := maps[j]
				if len(line) > 0{
					if unicode.IsDigit(rune(line[0])) && status { 
						numbers := strings.Split(line, (" "))
						dest, _ := strconv.Atoi(string(numbers[0]))
						source, _ := strconv.Atoi(string(numbers[1]))
						rangeee, _ := strconv.Atoi(string(numbers[2]))

						if seed >= source && seed < source+rangeee {
							diff := seed - source
							seed = (dest + diff)
							status = false
						}
					} else {
						status = true
					}
				}
			}
			if seed < min {
				min = seed
				Println("min=", seed)
			}
		}
	}
	Println()
	Println("minimo:", min)

}
