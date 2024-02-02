package middleware

import (
	"strings"
	"zecpos/internal/authentication"
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
)

func SessionMiddleware(c *fiber.Ctx) error {
	path := c.Path()

	if strings.HasPrefix(path, "/auth") {
		return c.Next()
	} else {
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
			if user.HasSuperAdminPermission() {
				return c.Redirect("/sa")
			}
		}

		c.Locals("user", user)
		return c.Next()
	}
}