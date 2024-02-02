package database

import (
	"gorm.io/gorm"
)

type Business struct {
	gorm.Model

	// Meta Data
	Title	 		string	`json:"title"`
	AccountsCount	int		`json:"accounts_count"`
	RenewalDate		string	`json:"renewal_date"`

	// Owner
	OwnerName		string	`json:"owner_name"`
	OwnerContact    string	`json:"owner_contact"`

	// Contact Person
	ContactPersonName		string	`json:"contact_person_name"`
	ContactPersonContact	string	`json:"contact_person_contact"`

	// Address
	AddressLine1	string	`json:"address_line1"`
	AddressLine2	string	`json:"address_line2"`
	City			string	`json:"city"`
	Province		string	`json:"province"`
}