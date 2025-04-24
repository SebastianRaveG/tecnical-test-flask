# 🚪 Inventario API - Prueba Técnica (Flask + PostgreSQL)

API REST para gestión de inventario entre tiendas y productos.  
Desarrollado en Flask con estructura modular, SQLAlchemy, PostgreSQL y principios SOLID.

---

## ⚙️ Instalación y configuración

1. Clona el repositorio con la estructura definida
2. Crea una nueva rama con tu nombre apartir de la main

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Configura la base de datos en un archivo `run.py`

```bash
app.config['SQLALCHEMY_DATABASE_URI'] = Las credenciales se dan a la hora de la prueba
```

5. Inicia las migraciones al tener los modelos construidos:

```bash
flask --app run:create_app db init
flask --app run:create_app db migrate
flask --app run:create_app db upgrade
```

6. Ejecuta la aplicación:

```bash
flask --app run:create_app run
```

7. Realiza las pruebas de los endpoint en postman
8. Sube la rama y lo que realizaste en esta.

---

---

## 📄 Estructura de tablas

### `Store`
- `id`: int (PK)
- `name`: str (único)

### `Product`
- `id`: int (PK)
- `name`: str (único)

### `StoreProduct`
- `id`: int (PK)
- `store_id`: FK a `Store`
- `product_id`: FK a `Product`
- `price`: float
- `inventory`: int

---

## Endpoints

### Tiendas `/stores`

| Método | Endpoint         | Descripción                     |
|--------|------------------|---------------------------------|
| GET    | `/stores/`       | Lista todas las tiendas         |
| GET    | `/stores/<id>/`  | Obtiene una tienda por ID       |
| POST   | `/stores/`       | Crea una tienda                 |
| PUT    | `/stores/<id>/`  | Actualiza una tienda            |
| DELETE | `/stores/<id>/`  | Elimina una tienda              |

### Productos `/products`

| Método | Endpoint           | Descripción                    |
|--------|--------------------|--------------------------------|
| GET    | `/products/`       | Lista todos los productos      |
| GET    | `/products/<id>/`  | Obtiene un producto por ID     |
| POST   | `/products/`       | Crea un producto               |
| PUT    | `/products/<id>/`  | Actualiza un producto          |
| DELETE | `/products/<id>/`  | Elimina un producto            |

### Productos por tienda `/store-products`

| Método | Endpoint                               | Descripción                                            |
|--------|-----------------------------------------|--------------------------------------------------------|
| GET    | `/store-products/`                      | Lista todas las relaciones producto/tienda             |
| GET    | `/store-products/<id>/`                 | Obtiene una relación específica                        |
| GET    | `/store-products/store/<store_id>/`     | Lista productos de una tienda con precio e inventario  |
| POST   | `/store-products/`                      | Crea una relación entre producto y tienda              |
| PUT    | `/store-products/<id>/`                 | Actualiza precio o inventario                          |
| DELETE | `/store-products/<id>/`                 | Elimina una relación                                   |

### Consultas con INNER JOIN (ENDPOINT)

| Método | Endpoint                                               | Descripción                                                |
|--------|--------------------------------------------------------|------------------------------------------------------------|
| GET    | `/store-products/products-in-store/<store_id>/`        | Lista productos con info extendida para una tienda         |
| GET    | `/store-products/product-info/<store_id>/<product_id>/`| Info de un producto específico en una tienda               |



## Extra (Opcional)

### Endpoint para registrar venta y actualizar inventario

| Método | Endpoint                                     | Descripción                                       |
|--------|----------------------------------------------|---------------------------------------------------|
| POST   | `/store-products/sell/`                      | Registra una venta y descuenta del inventario     |

#### Ejemplo del payload:

```json
{
  "store_id": 1,
  "product_id": 2,
  "quantity": 3
}
```

- Si hay suficiente inventario: lo descuenta y retorna `200 OK`.
- Si no hay inventario suficiente: retorna `400 Bad Request`.

---

## ✅ Buenas prácticas aplicadas

- Separación de lógica: controladores (views), servicios y modelos.
- Uso de Blueprints para organización de rutas.
- Código limpio y modular.
- Migrations con `Flask-Migrate`.
- Principios SOLID.


