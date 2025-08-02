# Django Security Measures

## 1. HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True` ensures all traffic is redirected to HTTPS.
- HSTS is enabled for one year using `SECURE_HSTS_SECONDS`, along with preload and subdomain inclusion.

## 2. Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are sent only over HTTPS.

## 3. HTTP Headers
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Protects against MIME-based attacks.
- `SECURE_BROWSER_XSS_FILTER`: Enables browser-level XSS protection.

## 4. Deployment
- Nginx is configured to redirect HTTP to HTTPS and serve with valid SSL certificates.
