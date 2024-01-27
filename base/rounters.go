package base

import "github.com/gofiber/fiber/v2"

func BaseRouters(app *fiber.App) {
	app.Get("/", IndexView)  // Index View
}