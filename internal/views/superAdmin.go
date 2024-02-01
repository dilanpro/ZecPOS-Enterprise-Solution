package views

import (
	"fmt"
	"strconv"
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
)

func SuperAdminView(c *fiber.Ctx) error {
	user := c.Locals("user").(database.User)
	fmt.Println(user)

	return c.SendString("Super Admin: " + strconv.FormatBool(user.HasSuperAdminPermission()))
}