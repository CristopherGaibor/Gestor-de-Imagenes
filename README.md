# - Sistema de Ingesta y Gestión de Imágenes (Etapa 2)

Este monorepositorio contiene la organización técnica y estructural para el entorno multiproyecto de BLISINUSS.

## 1. Diseño de la Arquitectura y Distribución de Responsabilidades
El sistema está diseñado bajo un enfoque de **Microservicios Desacoplados**, distribuyendo las responsabilidades de la siguiente manera:

* **`auth-service/` (Python - FastAPI):** Responsable único de la autenticación de usuarios, gestión de sesiones y emisión de credenciales de seguridad.
* **`image-service/` (Go - Gin/GORM):** Encargado del servicio de ingesta de archivos. Implementa **Arquitectura Hexagonal** para separar las reglas de negocio (Domain/Ports) de la infraestructura de almacenamiento y transporte (Adapters).
* **`network/`:** Módulo técnico para el mapeo, topología y simulación de la comunicación inter-servicio local.

## 2. Interacción de Componentes (Flujo de Trabajo)
1. El cliente envía una solicitud de subida a través del protocolo HTTP hacia el ecosistema.
2. El componente perimetral consulta con `auth-service` para verificar la validez de la sesión.
3. Tras la aprobación, `image-service` procesa el flujo binario (Multipart Form), extrae los metadatos técnicos (tamaño, resolución) y escribe el archivo físicamente en la capa de almacenamiento local optimizada (`uploads/`).

## 3. Catálogo de Endpoints Planificados
### Image Service
- `POST /api/v1/images/upload` -> Ingesta de archivos binarios y generación de metadatos técnicos.
- `GET /api/v1/images/` -> Recuperación y filtrado de metadatos indexados.
- `GET /api/v1/images/:id` -> Obtención detallada de metadatos de un archivo específico.

## 4. Convenciones de Nomenclatura y Criterios de Código
- **Ecosistema Go (`image-service`):** Uso de `camelCase` para variables locales y `PascalCase` para funciones o estructuras exportables. Formateo mandatorio mediante `go fmt`.
- **Ecosistema Python (`auth-service`):** Aplicación de la guía de estilo **PEP 8**, usando `snake_case` para variables y funciones.

## 5. Estrategia de Versionamiento (Git)
Para garantizar la integridad del código, el grupo implementa la metodología **GitHub Flow**:
- **Rama `main`:** Aloja únicamente código de producción e hitos estables evaluados por el docente.
- **Ramas de características (`feature/`)**: Cada integrante desarrollará módulos específicos de forma aislada (ej: `feature/router-auth`). Ningún cambio se integra a `main` sin un Pull Request verificado.