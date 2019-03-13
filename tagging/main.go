package main

import (
	"encoding/json"
	"fmt"
	"gopkg.in/yaml.v2"
)

func main() {
	var jsonBlob = []byte(`
	[
		{
			"animalName": "Platypus",
			"taxonomicOrder": "Monotremata"
		},
		{
			"animalName": "Quoll",
			"taxonomicOrder": "Dasyuromorphia"
		}
	]
`)
	type Animal struct {
		Name  string	`json:"animalName" yaml:"animal-name"`
		Order string	`json:"taxonomicOrder" yaml:"taxonomic-order"`
	}
	var animals []Animal
	err := json.Unmarshal(jsonBlob, &animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%+v\n", animals)
	d, err := yaml.Marshal(&animals)
	if err != nil {
		fmt.Println("error:", err)
	}
	fmt.Printf("%s",d)
}
