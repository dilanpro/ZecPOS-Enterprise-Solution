package views

import (
	"fmt"
	"strconv"
	"zecpos/internal/authentication"
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
)

func SuperAdminView(c *fiber.Ctx) error {
	user := authentication.LoggedUser(c)

	businesses := []database.Business{}
	database.GetDB().Find(&businesses)

	return c.Render("pages/super-admin-dashboard", fiber.Map{
		"User": user,
		"Businesses": businesses,
	})
}

func BusinessView(c *fiber.Ctx) error {
	user := authentication.LoggedUser(c)

	db := database.GetDB()

	businessId := c.Params("id")
	business := database.Business{}
	db.First(&business, businessId)

	switch c.Method() {
	case fiber.MethodGet:
		return c.Render("pages/business", fiber.Map{
			"User": user,
			"Business": business,
		})
	case fiber.MethodPost:

		title := c.FormValue("title")
		accountsCountStr := c.FormValue("account-count")
		accountsCount, _ := strconv.Atoi(accountsCountStr)
		renewalDate := c.FormValue("renewal-date")

		ownerName := c.FormValue("owner-name")
		ownerContact := c.FormValue("owner-contact")

		contactPersonName := c.FormValue("contact-person-name")
		contactPersonContact := c.FormValue("contact-person-contact")

		addressLine1 := c.FormValue("address-line-1")
		addressLine2 := c.FormValue("address-line-2")
		city := c.FormValue("city")
		province := c.FormValue("province")

		business.Title = title
		business.AccountsCount = accountsCount
		business.RenewalDate = renewalDate
		business.OwnerName = ownerName
		business.OwnerContact = ownerContact
		business.ContactPersonName = contactPersonName
		business.ContactPersonContact = contactPersonContact
		business.AddressLine1 = addressLine1
		business.AddressLine2 = addressLine2
		business.City = city
		business.Province = province

		db.Save(&business)

		return c.Redirect(fmt.Sprintf("/sa/business/%d", business.ID))


	default:
		return c.Status(fiber.StatusMethodNotAllowed).SendString("Method Not Allowed")
	}
}