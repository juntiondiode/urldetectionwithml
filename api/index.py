from app import app as application
from vercel_python_wsgi import vercel_handler

def handler(event, context):
    return vercel_handler(event, context, application)
