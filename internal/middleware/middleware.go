package middleware

import (
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)

func SessionMiddleware(c *fiber.Ctx) error {

	// All endpoints other than auth/login are protected
	username := session.GetSession(c, "username")
	if c.Path() != "/auth/login" && username == "" {
		return c.Redirect("/auth/login")
	}

	return c.Next()
}