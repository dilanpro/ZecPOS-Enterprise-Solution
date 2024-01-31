package session

import (
	"time"
	"zecpos/internal/database"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/session"
	"github.com/gofiber/storage/mysql/v2"
)

var storage = mysql.New(mysql.Config{
	ConnectionURI:   database.DNS,
	Reset:           false,
	GCInterval:      10 * time.Second,
})
var SessionStore = session.New(session.Config{
    Storage: storage,
})

func InitSession(c *fiber.Ctx) (*session.Session) {
	sess, err := SessionStore.Get(c)
	if err != nil {
		panic(err)
	}
	return sess
}

func GetSession(c *fiber.Ctx, key string) (interface{}) {
	sess := InitSession(c)
	value := sess.Get(key)
	if value == nil {
		return ""
	}
	return value
}

func SetSession(c *fiber.Ctx, key string, value interface{}) {
	sess := InitSession(c)
	sess.Set(key, value)
	sess.Save()
}

func FlushSession(c *fiber.Ctx) {
	sess := InitSession(c)
	if err := sess.Destroy(); err != nil {
        panic(err)
    }
}

