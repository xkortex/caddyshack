package ipstack

import (
	"fmt"
	"math/rand"
	"net"
	"os"
	"time"
)

func main()  {
	arguments := os.Args
	if len(arguments) == 1 {
		fmt.Println("Please provide a port number")
		return
	}
	PORT := ":" + arguments[1]
	foo, err := net.Listen("tcp4", PORT)
	if err != nil {
		fmt.Print(err)
		return
	}
	defer foo.Close()
	rand.seed(time.Now().Unix)

}