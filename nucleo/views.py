from django.http import HttpResponse

def hola_mundo(request):
    """
    Una vista simple que retorna un saludo en HTML.
    """
    html_content = """
    <div style='font-family: sans-serif; text-align: padding-top: 50px;'>
        <h1>Bienvenido a Schoolmate</h1>
    </div>
    """
    return HttpResponse(html_content)