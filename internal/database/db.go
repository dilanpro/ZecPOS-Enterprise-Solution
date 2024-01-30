package database

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)


var DB *gorm.DB
var err error

const DNS = "root:@tcp(127.0.0.1:3306)/godb?charset=utf8mb4&parseTime=True&loc=Local"

func GetDB() *gorm.DB {
	if DB == nil {
		DB, err = gorm.Open(mysql.Open(DNS), &gorm.Config{})
		if err != nil {
			fmt.Println(err.Error())
			panic("Could not connect to the database")
		}
	}

	return DB

}
