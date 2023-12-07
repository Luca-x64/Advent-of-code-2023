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
	if err == nil {
		scanner := bufio.NewScanner(file)
		var lines []string
		for scanner.Scan() {
			line := scanner.Text()
			if len(line) > 0 {
				lines = append(lines, line)
			}
		}

		var struttura [][][]string
		seedstring := strings.Split(lines[0], " ")[1:]
		var seeds []int
		for s := range seedstring {
			convert, _ := strconv.Atoi(seedstring[s])
			seeds = append(seeds, convert)
		}

		var mappa [][]string
		for i := range lines {
			if unicode.IsDigit(rune(lines[i][0])) { // numeri
				mappa = append(mappa, strings.Split(lines[i], (" ")))
			} else { // nuova mappa
				if len(mappa) > 0 {
					struttura = append(struttura, mappa)
					mappa = [][]string{}
				}
			}
		}
		struttura = append(struttura, mappa)

		for i := 0; i < len(struttura); i++ {
			var history []int
			for j := 0; j < len(struttura[i]); j++ {
				for s := 0; s < len(seeds); s++ {

					dest, _ := strconv.Atoi(struttura[i][j][0])
					source, _ := strconv.Atoi(struttura[i][j][1])
					rangee, _ := strconv.Atoi(struttura[i][j][2])

					if seeds[s] >= source && seeds[s] < source+rangee && slices.Index(history, s) == -1 {
						diff := seeds[s] - source
						seeds[s] = (dest + diff)
						history = append(history, s)
					}
				}
			}
		}
		min := 100000000000000
		for i := 0; i < len(seeds); i++ {
			if min > seeds[i] {
				min = seeds[i]
			}
		}
		Println("minimo:", min)
	}
}
