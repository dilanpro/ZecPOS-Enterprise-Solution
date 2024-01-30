package main

import (
	"zecpos/internal/middleware"
	"zecpos/internal/routers"

	"github.com/gofiber/fiber/v2"

	"github.com/gofiber/template/html/v2"
)


func main() {

	engine := html.New("../web/templates", ".html")



	app := fiber.New(fiber.Config{
		Views: engine,
	})
	app.Use(middleware.SessionMiddleware)
	routers.Router(app)


	app.Listen(":3000")

}