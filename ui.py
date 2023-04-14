import atexit
import subprocess as sp
import os
import webview


def __kill_server(p):
    if os.name == 'nt':
        # p.kill is not adequate
        sp.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
    elif os.name == 'posix':
        p.kill()
    else:
        pass


if __name__ == '__main__':
    cmd = f'streamlit run app.py --server.headless=True'

    p = sp.Popen(cmd.split(), stdout=sp.DEVNULL)
    atexit.register(__kill_server, p)

    hostname = 'localhost'
    port = 8501

    # noinspection HttpUrlsUsage
    webview.create_window(
        title='ZecPOS | The Most Affordable POS System',
        url=f"http://{hostname}:{port}",
        width=1280,
        height=720,
        min_size=(600, 800),
        # TODO: Remove this
        x=-1550,
        y=1200
    )
    webview.start()
