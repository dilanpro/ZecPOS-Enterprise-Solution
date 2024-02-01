package views

import (
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
)

func SuperAdminView(c *fiber.Ctx) error {
	user := c.Locals("user").(database.User)

	return c.Render("pages/super-admin-dashboard", fiber.Map{
		"user": user,
	})
}