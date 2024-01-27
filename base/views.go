package base

import "github.com/gofiber/fiber/v2"

func IndexView(c *fiber.Ctx) error {
	return c.SendString("Hello, World! Again")
}