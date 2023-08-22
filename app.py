
from app import create_app
import webview


if __name__ == '__main__':
    # webview.create_window(
    #     "ZecPOS | Enterprise POS Solution",
    #     create_app()
    # )
    # webview.start()
    create_app().run(debug=True)
