package handler

import (
	"encoding/json"
	"image-service/internal/core/ports"
	"net/http"
)

type HTTPHandler struct {
	imageService ports.ImageService
}

func NewHTTPHandler(service ports.ImageService) *HTTPHandler {
	return &HTTPHandler{imageService: service}
}

func (h *HTTPHandler) UploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Método no permitido", http.StatusMethodNotAllowed)
		return
	}

	token := r.Header.Get("Authorization")
	if token == "" {
		http.Error(w, "No autorizado: Falta token de autenticación", http.StatusUnauthorized)
		return
	}

	err := r.ParseMultipartForm(10 << 20)
	if err != nil {
		http.Error(w, "Error al procesar el formulario masivo", http.StatusBadRequest)
		return
	}

	file, handler, err := r.FormFile("image")
	if err != nil {
		http.Error(w, "No se encontró el campo 'image' en la petición", http.StatusBadRequest)
		return
	}
	defer file.Close()

	userID := "user_123"
	img, err := h.imageService.UploadImage(handler.Filename, handler.Size, file, userID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(img)
}
