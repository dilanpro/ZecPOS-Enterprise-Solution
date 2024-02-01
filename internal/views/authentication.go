package views

import (
	"zecpos/internal/database"
	"zecpos/internal/session"

	"github.com/gofiber/fiber/v2"
)


func AuthorizeRequest(c *fiber.Ctx) database.User {
	username := session.GetSession(c, "username")
	if username == "" {
		panic("User authorization failed")
	}

	DB := database.GetDB()
	var user database.User
	DB.First(&user, "username = ?", username)

	return user
}


func LoginView(c *fiber.Ctx) error {

	switch c.Method() {
	case fiber.MethodGet:
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

		// Set Session
		session.SetSession(c, "username", user.Username)

		return c.Redirect("/")  // TODO: Implement the Route for this

	default:
		return c.Status(fiber.StatusMethodNotAllowed).SendString("Method Not Allowed")
	}
}

func LogoutView(c *fiber.Ctx) error {
	session.FlushSession(c)
	return c.Redirect("/auth/login")
}