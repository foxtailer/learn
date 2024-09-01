from aiohttp import web

async def handle(request):
    # Print request details
    print(f"Method: {request.method}")
    print(f"Path: {request.path}")
    print(f"Headers: {request.headers}")
    print(type(request))
    print(request)
    
    # If there is a query string, print it
    if request.query_string:
        print(f"Query String: {request.query_string}")
    
    # If the request has a body, read and print it
    if request.can_read_body:
        body = await request.text()
        print(f"Body: {body}")
    
    # Send a response back to the browser
    return web.Response(text="Request received and printed in the console")

# Create an aiohttp web application
app = web.Application()

# Add a route that uses the handler
app.router.add_get('/', handle)

# Run the web application
if __name__ == '__main__':
    web.run_app(app, port=8080)
