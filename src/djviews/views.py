from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
#     print(request)
#     print(dir(request))

#     print(request.method)
#     print(request.is_ajax)
#     print(request.is_ajax())
#     print(request.get_full_path())

#     return HttpResponse('''
#         <!DOCTYPE html>
#         <head>
#             <style>
#                 h1 {
#                     color: red;
#                 }
#             </style>
#         </head>

#         <body>
#             <h1>Hello, from Home!</>
#         </body>
#         </html>
#     ''')


def home(request):
    response = HttpResponse(content_type='text/html')
    # response = HttpResponse(content_type = 'application/json')

    # response.content('<!DOCTYPE html><head><style>h1{color: red;}</style></head><body><h1>Hello, from Home!</></body></html>')

    print(response.status_code)
    response.write('<h1>Page Not Found!</h1>')

    response.status_code = 404
    return response


def redirect_somewhere(request):
    return HttpResponseRedirect('https://stackoverflow.com')
