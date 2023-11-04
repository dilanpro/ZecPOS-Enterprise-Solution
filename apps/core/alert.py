from django.http import HttpResponse
from django_htmx.http import retarget


def success(message: str, content: str = ""):
    success_message: str = content + (
        '<script>Toastify({text: "'
        + str(message)
        + '", duration: 5000, gravity: "top", position: "center"}).showToast();</script>'
    )
    response = HttpResponse(success_message)
    return retarget(response, "#alert")


def error(message: str, content: str = ""):
    success_message: str = content + (
        '<script>Toastify({text: "'
        + str(message)
        + '", duration: 5000, gravity: "top", position: "center", backgroundColor: "#fca5a5"}).showToast();</script>'
    )
    response = HttpResponse(success_message)
    return retarget(response, "#alert")
