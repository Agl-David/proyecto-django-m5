# Sistema de Reservas - Django 🗓️

## 📌 Descripción

API REST desarrollada con Django y Django Rest Framework para gestionar reservas de servicios.

---

## 🚀 Funcionalidades

* CRUD de usuarios
* CRUD de servicios
* CRUD de horarios
* CRUD de reservas
* API personalizada: reservas del día
* Validación para evitar reservas duplicadas

---

## 🧠 Tecnologías

* Python
* Django
* Django Rest Framework

---

## 📦 Instalación

```bash
git clone <TU_REPO_URL>
cd proyecto
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔗 Endpoints

* /api/usuarios/
* /api/servicios/
* /api/horarios/
* /api/reservas/
* /api/reservas-hoy/

---

## 🧪 Ejemplo de respuesta

```json
[
  {
    "usuario": "Jose",
    "servicio": "corte",
    "hora": "12:00:00 - 18:00:00"
  }
]
```

---

## 👨‍💻 Autor

David Adrian Aguilar Loza
