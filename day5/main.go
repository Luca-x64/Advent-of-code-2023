package main

import (
	"bufio"
	. "fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	file, err := os.Open("test.txt")
	if err == nil {
		scanner := bufio.NewScanner(file)
		lines := []string{}
		for scanner.Scan() {
			line := scanner.Text()
			if len(line) > 0 {
				lines = append(lines, line)
			}
		}
		var struttura [][][]string 
		seedstring := strings.Split(lines[0], " ")[1:]
		seeds := []int{}
		for s := range seedstring {
			convert, _ := strconv.Atoi(seedstring[s])
			seeds = append(seeds, convert)
		}
		Println("seeds:", seeds)
		mappa := [][]string{}
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
		//Println(lines)
		//Print(struttura)
		//Println(struttura)
		for i := 0; i < len(struttura); i++ {
			Println(i+1)
			//nochanges := true
			for j := 0; j < len(struttura[i]); j++ {
				for s := 0; s < len(seeds); s++ {
					seme := seeds[s]
					dest, _ := strconv.Atoi(struttura[i][j][0])
					source, _ := strconv.Atoi(struttura[i][j][1])
					rangee, _ := strconv.Atoi(struttura[i][j][2])
					//Println(source,dest,rangee)
					if seme >= source && seme < source+rangee {
						diff := seme - source
						seeds[s] = dest + diff
						//nochanges = false
						Println(seme,diff,dest, source, rangee, seeds)
					}
				}
			}
			// if nochanges{
			// 	seeds[s] = s
			// }
			//Println("seeds:",seeds)
		}
		Println(min(seeds[0], seeds[1], seeds[2], seeds[3]))
		Println(seeds)
	}

	//file,nil := os.Open("input.txt")
}
