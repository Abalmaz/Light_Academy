import shortly
from shortly import create_app


application = create_app()
# def application(env, start_response):
#     # start_response('200 OK', [('Content-Type','text/html')])
#     application = create_app()
#     # return [b"Hello World"]