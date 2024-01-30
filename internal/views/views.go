package views

import (
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)

type User struct {
	Username string
}

func IndexView(c *fiber.Ctx) error {
	println("IndexView", c.Locals("username").(string))
	session.SetSession(c, "username", "madhavi")

	return c.Render("index", fiber.Map{
		"Title": "Hello, World from Django!",
		"Numbers": []int{1, 2, 3, 4, 5},
	})
}

func GetView(c *fiber.Ctx) error {
	println("GetView", c.Locals("username").(string))
	return c.SendString("Hello")
}