package views

import (
	"github.com/gofiber/fiber/v2"
)


func IndexView(c *fiber.Ctx) error {
	user := AuthorizeRequest(c)

	return c.JSON(user)
}