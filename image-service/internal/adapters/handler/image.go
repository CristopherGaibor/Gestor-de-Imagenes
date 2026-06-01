package handler

import (
	"net/http"
	"path/filepath"

	"github.com/gin-gonic/gin"
)

func UploadImage(c *gin.Context) {

	file, err := c.FormFile("file")
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "No se recibió ninguna imagen :)"})
		return
	}

	filename := filepath.Base(file.Filename)

	destination := "uploads/" + filename

	if err := c.SaveUploadedFile(file, destination); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Fallo interno al guardar la imagen"})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"message":  "Imagen procesada y guardada exitosamente",
		"filename": filename,
	})
}
