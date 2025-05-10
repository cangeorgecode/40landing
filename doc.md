# Documentation draft

## Token for DRF

```
# Get a token
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://127.0.0.1:8000/api/token/


# Use the token
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://127.0.0.1:8000/api/tenants/
```


&nbsp;


