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
	//file, err := os.Open("test.txt")
	file, err := os.Open("input.txt")
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
		//Println("seeds:", seeds)
		mappa := [][]string{}
		for i := range lines {
			if unicode.IsDigit(rune(lines[i][0])) { // numeri
				mappa = append(mappa, strings.Split(lines[i], (" ")))
			} else { // nuova mappa
				if len(mappa) > 0 {

					//sort mappa
					for line := 0; line < len(mappa)-1; line++ {
						for item := 0; item < len(mappa)-1; item++ {
							a,_ := strconv.Atoi(mappa[item][0])
							b,_ := strconv.Atoi(mappa[item+1][0])
							Println(a,b)
							if a > b{
								mappa[item],mappa[item+1] = mappa[item+1],mappa[item]
							} 
						}
					}

					struttura = append(struttura, mappa)
					mappa = [][]string{}
				}
			}
		}
		struttura = append(struttura, mappa)
		//Println(lines)
		Print(struttura)
		//Println(struttura)
		for i := 0; i < len(struttura); i++ {
			//Println(i+1)
			//nochanges := true
			for j := 0; j < len(struttura[i]); j++ {
				for s := 0; s < len(seeds); s++ {
					seme := seeds[s]
					dest, _ := strconv.Atoi(struttura[i][j][0])
					source, _ := strconv.Atoi(struttura[i][j][1])
					rangee, _ := strconv.Atoi(struttura[i][j][2])
					//Print(dest,source,rangee,",")
					if seme >= source && seme < source+rangee {
						diff := seme - source
						seeds[s] = dest + diff
						//nochanges = false
						//Println(seme,diff,dest, source, rangee, seeds)
						//Println("\t",seme," =>  ",seeds[s])
					}
				}
				//Println()
			}
			//Println("seeds:",seeds)
			// if nochanges{
			// 	seeds[s] = s
			// }
			//Println("seeds:",seeds)
		}
		//Println(min(seeds[0], seeds[1], seeds[2], seeds[3]))
		//Println(seeds)
		min := 100000000000000
		for i := 0; i < len(seeds); i++ {
			if min > seeds[i]{
				min = seeds[i]
			}
		}
		Println(min)
	}

	//file,nil := os.Open("input.txt")
}
