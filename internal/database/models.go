package database

import "gorm.io/gorm"

type Person struct {
	gorm.Model
	FirstName string	`json:"first_name"`
	LastName  string	`json:"last_name"`
	Email     string	`json:"email"`
}

type Teacher struct {
	gorm.Model
	FirstName string	`json:"first_name"`
	LastName  string	`json:"last_name"`
	Email     string	`json:"email"`
}