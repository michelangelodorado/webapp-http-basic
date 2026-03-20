# webapp-http-basic

A simple Flask webapp protected with HTTP Basic authentication, packaged in a Docker container.

## Credentials

| Username | Password |
|----------|----------|
| admin    | admin    |
| user     | password |

## Usage

### Build and Run

```bash
docker build -t webapp-http-basic .
docker run -d \
  --name webapp-http-basic \
  --restart unless-stopped \
  -p 80:80 \
  webapp-http-basic
```

### Test

```bash
curl -u admin:admin http://localhost:8080
```

Or open http://localhost:8080 in your browser — you'll be prompted for credentials.

### Stop

```bash
docker stop webapp-http-basic && docker rm webapp-http-basic
```
