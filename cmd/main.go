package main

import (
	"os"
	"path/filepath"
	"zecpos/internal/middleware"
	"zecpos/internal/routers"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)


func main() {

	dir, err := os.Getwd()
	if err != nil {
		panic("Error getting current directory:" + err.Error())
	}
	engine := html.New("web/templates", ".html")
	if filepath.Base(dir) == "cmd" {
		engine = html.New("../web/templates", ".html")
	}

	app := fiber.New(fiber.Config{
		Views: engine,
	})
	app.Use(middleware.SessionMiddleware)
	routers.Router(app)

	app.Listen(":8000")

}