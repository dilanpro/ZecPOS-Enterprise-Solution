package routers

import (
	"zecpos/internal/views"

	"github.com/gofiber/fiber/v2"
)

func DashboardRouter(app *fiber.App) {
	app.Get("", views.IndexView)
}