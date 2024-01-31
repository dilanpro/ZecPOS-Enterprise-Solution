package database

import (
	"gorm.io/gorm"
	"golang.org/x/crypto/bcrypt")

type User struct {
	gorm.Model
	Username 		string		`json:"username"`
	Password		string		`json:"password"`
	Name     		string		`json:"Name"`
	IsSuperAdmin	bool		`json:"is_super_admin"`
}


func (u *User) Create() {
	db := GetDB()

	passwordHash, err := bcrypt.GenerateFromPassword([]byte(u.Password), bcrypt.DefaultCost)
	if err != nil {
		panic("Could not hash password")
	}
	u.Password = string(passwordHash)

	db.Create(u)
}

func (u *User) CheckPassword(password string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(u.Password), []byte(password))
	return err == nil
}