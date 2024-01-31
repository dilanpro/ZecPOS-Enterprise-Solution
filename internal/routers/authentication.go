package routers

import (
	"zecpos/internal/views"

	"github.com/gofiber/fiber/v2"
)

func Router(app *fiber.App) {
	app.All("auth" + "/login", views.LoginView)
}