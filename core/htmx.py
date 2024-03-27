from dataclasses import dataclass
from typing import Any, List

from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import render_to_string
from django_htmx.http import retarget
from render_block import render_block_to_string


@dataclass
class HtmxRenderObject:
    """
    Base class for htmx objects.
    :param template_name: The name of the template to render.
    :param context: The context to render the block with.
    """

    template_name: str
    context: dict | None = None

    def __post_init__(self):
        if self.context is None:
            self.context = {}

    def render(self, request) -> str:
        raise NotImplementedError("Please implement this method.")


@dataclass
class HtmlStringObject:
    """
    A class to render a string/html as a string.
    :param html_string: The html string to render.
    """

    html_string: str | Any

    def __post_init__(self):
        if not isinstance(self.html_string, str):
            self.html_string = str(self.html_string)

    def render(self, request) -> str:
        return self.html_string


@dataclass
class BlockObject(HtmxRenderObject):
    """
    A class to render a block from a template as a string.
    :param block_name: The name of the block to render.
    :param context: The context to render the block with.
    """

    block_name: str = "[Block Name Required]"

    def render(self, request) -> str:
        return render_block_to_string(
            self.template_name,
            self.block_name,
            self.context,
            request=request,
        )


@dataclass
class TemplateObject(HtmxRenderObject):
    """
    A class to render a complete template as a string.
    :param context: The context to render the template with.
    """

    def render(self, request) -> str:
        return render_to_string(
            self.template_name,
            self.context,
            request=request,
        )


def BadRequest() -> HttpResponseBadRequest:
    """
    Returns an HttpResponseBadRequest object.
    """
    return HttpResponseBadRequest()


def Response(
    request,
    htmx_objects: List[HtmxRenderObject | HtmlStringObject] | None = None,
    success_message: str = "",
    error_message: str = "",
    redirect_uri: str = "",
) -> HttpResponse:
    """
    A function to render a list of partials and return them as an HttpResponse.

    Special Note: Please follow the below instructions to use this function.
        - Stuck to Out of Band Swap (hx-swap-oob) and make sure you provide proper IDs to the partials.
        - Don't add hx-target to the html elements
        - Don't add hx-swap to the html elements
        - Create a empty div with id #alert in the base template and make sure it is inherited into every template.
    Caution: If you break any rule mentioned above, wired things will happen (because it swaps with #alert).

    :param request: The request object.
    :param htmx_objects: A list of htmx.TemplateObject or htmx.BlockObject objects.
    :param success_message: A success message to display in a toast (optional).
    :param error_message: An error message to display in a toast (optional, will be avoided if success_message is present).
    :return: An HttpResponse object.
    """

    if htmx_objects is None:
        htmx_objects = []

    template_str: str = "\n\n".join(
        [partial_object.render(request) for partial_object in htmx_objects]
    )

    if success_message:
        template_str += f'<script>Toastify({{text: "{success_message}", duration: 5000, gravity: "top", position: "center"}}).showToast();</script>'
    elif error_message:
        template_str += f'<script>Toastify({{text: "{error_message}", duration: 5000, gravity: "top", position: "center", backgroundColor: "#fca5a5"}}).showToast();</script>'
    else:
        template_str += '<div id="alert"></div>'

    if redirect_uri:
        template_str += f'<script>window.location.href = "{redirect_uri}";</script>'
    else:
        template_str += '<div id="hx-redirects"></div>'

    return retarget(response=HttpResponse(template_str), target="#alert")
