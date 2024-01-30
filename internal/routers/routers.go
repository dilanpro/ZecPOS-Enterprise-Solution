package routers

import (
	"zecpos/internal/views"

	"github.com/gofiber/fiber/v2"
)

func Router(app *fiber.App) {
	app.Get("", views.IndexView)
	app.Get("session", views.GetView)
}