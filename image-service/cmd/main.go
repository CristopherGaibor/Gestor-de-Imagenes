package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	v1 := r.Group("/api/v1/images")
	{
		v1.POST("/upload", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "Endpoint de Ingesta (Fase de Diseño)"})
		})

		v1.GET("/", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "Endpoint de Listado (Fase de Diseño)"})
		})

		v1.GET("/:id", func(c *gin.Context) {
			c.JSON(http.StatusOK, gin.H{"message": "Endpoint de Consulta por ID (Fase de Diseño)"})
		})
	}

	r.Run(":8080")
}
