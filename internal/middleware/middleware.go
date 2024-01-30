package middleware

import (
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)

func SessionMiddleware(c *fiber.Ctx) error {
	username := session.GetSession(c, "username")
	c.Locals("username", username)

	return c.Next()
}