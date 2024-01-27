package main

import (
	"ZecPOS/base"
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/django/v3"
)

func main() {
	engine := django.New("./templates", ".django")

	app := fiber.New(fiber.Config{
        Views: engine,
    })

	app.Static("/static", "./static")

	// Register Base Routers
	base.BaseRouters(app)

	log.Fatal(app.Listen(":8000"))
}