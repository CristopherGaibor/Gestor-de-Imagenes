package main

import (
	"image-service/internal/handler"

	"github.com/gin-gonic/gin"
)

func main() {

	router := gin.Default()

	router.POST("/upload", handler.UploadImage)

	router.Run(":5000")
}
