package main

import (
	"os"
	"path/filepath"
	"zecpos/internal/database"
	"zecpos/internal/middleware"
	"zecpos/internal/routers"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)


func main() {

	// Defining Web Directory Path
	dir, err := os.Getwd()
	if err != nil {
		panic("Error getting current directory:" + err.Error())
	}
	webPath := ""
	if filepath.Base(dir) == "cmd" {
		webPath = "../"
	}

	// Initiate Template Engine
	engine := html.New(webPath + "web/templates", ".html")

	// Initial DB Migration
	database.Migrate()

	// Initiating App
	app := fiber.New(fiber.Config{
		Views: engine,
	})

	// Loading Statics
	app.Static("/static", webPath + "web/static")


	app.Use(middleware.SessionMiddleware)
	routers.AuthRouter(app)
	routers.DashboardRouter(app)

	app.Listen(":8000")

}