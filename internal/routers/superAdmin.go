package routers

import (
	"zecpos/internal/views"

	"github.com/gofiber/fiber/v2"
)

func SuperAdminRouter(app *fiber.App) {
	app.Get("sa", views.SuperAdminView)
	app.All("sa/business/:id", views.BusinessView)
}