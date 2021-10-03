from app import app
from secure import SecureHeaders
secure_headers = SecureHeaders()

@app.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response
