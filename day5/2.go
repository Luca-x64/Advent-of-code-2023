package main

import (
	"bufio"
	. "fmt"
	"os"
	"slices"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	//file, err := os.Open("test.txt")
	file, err := os.Open("input.txt")
	var seeds []int
	if err == nil {
		scanner := bufio.NewScanner(file)

		cnt := 0
		var seedstring []string
		scanner.Scan()
		line := scanner.Text()
		seedstring = strings.Split(line, " ")[1:]
		for i := 0; i < len(seedstring)-1; i += 2 {
			seed, _ := strconv.Atoi(seedstring[i])
			rangee, _ := strconv.Atoi(seedstring[i+1])
			for s := 0; s < rangee; s++ {
				seeds = append(seeds, seed+s)

			}
		}

		var mappa [][]string
		for scanner.Scan() {
			line := scanner.Text()
			if len(line) > 0 {
				Print()
				if unicode.IsDigit(rune(line[0])) { // numeri
					mappa = append(mappa, strings.Split(line, (" ")))
				} else { // nuova mappa
					if len(mappa) > 0 {
					Println("m", mappa)
					var history []int

					for m := range mappa {
						for s := 0; s < len(seeds); s++ {

							dest, _ := strconv.Atoi(mappa[m][0])
							source, _ := strconv.Atoi(mappa[m][1])
							rangee, _ := strconv.Atoi(mappa[m][2])

							if seeds[s] >= source && seeds[s] < source+rangee && slices.Index(history, s) == -1 {
								diff := seeds[s] - source
								seeds[s] = (dest + diff)
								history = append(history, s)
							}
						}
					}
					}
					mappa = [][]string{}
				}
			}
			cnt += 1
		}
	}
	Println()
	Println(seeds)
	min := 100000000000000
	for i := 0; i < len(seeds); i++ {
		if min > seeds[i] {
			min = seeds[i]
		}
	}
	Println("minimo:", min)
}
