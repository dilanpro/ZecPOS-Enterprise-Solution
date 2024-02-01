package views

import (
	"github.com/gofiber/fiber/v2"
)


func IndexView(c *fiber.Ctx) error {
	user := c.Locals("user")
	return c.JSON(user)
}