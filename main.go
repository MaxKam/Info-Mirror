package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/spf13/viper"
)

func main() {
	viper.SetConfigName("config")    // name of config file (without extension)
	viper.SetConfigType("yaml")      // REQUIRED if the config file does not have the extension in the name
	viper.AddConfigPath("./config/") // path to look for the config file in
	viper.AddConfigPath(".")         // optionally look for config in the working directory
	err := viper.ReadInConfig()      // Find and read the config file
	if err != nil {                  // Handle errors reading the config file
		panic(fmt.Errorf("fatal error config file: %s", err))
	}
	viper.WatchConfig()

	server := gin.Default()
	server.Static("/assets", "./assets")
	server.LoadHTMLGlob("templates/*")

	// Home page
	server.GET("/", func(c *gin.Context) {
		c.HTML(
			http.StatusOK,
			"index.html",
			gin.H{},
		)
	})

	server.Run()
}
