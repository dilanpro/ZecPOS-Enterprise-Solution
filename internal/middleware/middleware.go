package middleware

import (
	"strings"
	"zecpos/internal/authentication"
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
)

func SessionMiddleware(c *fiber.Ctx) error {
	path := c.Path()

	if path != "/auth/login" {
		var user database.User
		var err error

		if strings.HasPrefix(path, "/sa") {
			user, err = authentication.SuperAdminAuthorizeRequest(c)
			if err != nil {
				return c.SendStatus(fiber.StatusUnauthorized)
			}
		} else {
			user, err = authentication.AuthorizeRequest(c)
			if err != nil {
				return c.Redirect("/auth/login")
			}
		}

		c.Locals("user", user)
	}

	return c.Next()
}