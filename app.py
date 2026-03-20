from flask import Flask, request, Response

app = Flask(__name__)

USERS = {
    "admin": "admin",
    "user": "password",
}


def check_auth(username, password):
    return USERS.get(username) == password


def authenticate():
    return Response(
        "Authentication required.",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )


@app.before_request
def require_basic_auth():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()


@app.route("/")
def index():
    user = request.authorization.username
    return f"""<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
    <h1>Hello, {user}!</h1>
    <p>You are authenticated via HTTP Basic Auth.</p>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
