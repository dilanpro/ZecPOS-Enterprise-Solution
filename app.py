
from app import create_app
import webview

if __name__ == '__main__': 
	webview.create_window(
		"ZecPOS",
		create_app()
	)
	webview.start()
