package views

import (
	"zecpos/internal/database"
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)

func LoginView(c *fiber.Ctx) error {

	switch c.Method() {
	case fiber.MethodGet:
		println("IndexView", c.Locals("username").(string))
		session.SetSession(c, "username", "madhavi")
		return c.Render("pages/login", fiber.Map{})

	case fiber.MethodPost:
		username := c.FormValue("username")
		password := c.FormValue("password")

		DB := database.GetDB()
		var user database.User
		DB.First(&user, "username = ?", username)

		// User not found
		if user.Username == "" {
			return c.Render("pages/login", fiber.Map{
				"Username": username,
				"Password": password,
				"Error": "Invalid username or password",
			})
		}

		// Check password
		if !user.CheckPassword(password) {
			return c.Render("pages/login", fiber.Map{
				"Username": username,
				"Password": password,
				"Error": "Invalid username or password",
			})
		}

		return c.Redirect("/")  // TODO: Implement the Route for this

	default:
		return c.Status(fiber.StatusMethodNotAllowed).SendString("Method Not Allowed")
	}
}

func GetView(c *fiber.Ctx) error {
	println("GetView", c.Locals("username").(string))
	return c.SendString("Hello")
}