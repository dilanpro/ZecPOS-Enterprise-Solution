package authentication

import (
	"zecpos/internal/database"
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)


func AuthorizeRequest(c *fiber.Ctx) (database.User, error) {
	username := session.GetSession(c, "username")
	if username == "" {
		return database.User{}, fiber.NewError(fiber.StatusUnauthorized, "Unauthorized as User")
	}

	DB := database.GetDB()
	var user database.User
	DB.First(&user, "username = ?", username)

	return user, nil
}

func SuperAdminAuthorizeRequest(c *fiber.Ctx) (database.User, error) {
	user, err := AuthorizeRequest(c)
	if err != nil || !user.HasSuperAdminPermission() {
		return database.User{}, fiber.NewError(fiber.StatusUnauthorized, "Unauthorized as Super Admin")
	}

	return user, nil
}