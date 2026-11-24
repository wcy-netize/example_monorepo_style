package main

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"service": "c", "ok": true})
	})

	router.GET("/file", func(c *gin.Context) {
		name := c.Query("name")
		data, err := os.ReadFile(name)
		if err != nil {
			c.String(http.StatusBadRequest, err.Error())
			return
		}
		c.String(http.StatusOK, string(data))
	})

	router.GET("/hash", func(c *gin.Context) {
		value := c.Query("value")
		sum := md5.Sum([]byte(value))
		c.String(http.StatusOK, fmt.Sprintf("%x", sum))
	})

	router.Run(":8080")
}
