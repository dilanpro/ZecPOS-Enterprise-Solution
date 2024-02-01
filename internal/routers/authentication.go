package routers

import (
	"zecpos/internal/views"

	"github.com/gofiber/fiber/v2"
)

func AuthRouter(app *fiber.App) {
	app.All("auth/login", views.LoginView)
	app.All("auth/logout", views.LogoutView)
}