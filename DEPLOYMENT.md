# Deployment Guide for AIPS

This guide explains how to deploy the Agricultural Intelligence Prediction System in different environments.

## Local Development

### Quick Start
```bash
# Clone the repository
git clone https://github.com/abdulraheem2006/AGRICULTURAL-INTELLIGENCE-PREDICTION-SYSTEM.git
cd AGRICULTURAL-INTELLIGENCE-PREDICTION-SYSTEM

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

## Production Deployment

### Using Gunicorn (Recommended for Linux)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Waitress (Recommended for Windows)

1. Install Waitress:
```bash
pip install waitress
```

2. Create a production server file `wsgi.py`:
```python
from waitress import serve
from app import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
```

3. Run:
```bash
python wsgi.py
```

## Docker Deployment

### Dockerfile
Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build and Run
```bash
# Build the image
docker build -t aips:latest .

# Run the container
docker run -d -p 5000:5000 aips:latest
```

## Cloud Deployment

### Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add `gunicorn` to `requirements.txt`

3. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### AWS Elastic Beanstalk

1. Install EB CLI:
```bash
pip install awsebcli
```

2. Initialize and deploy:
```bash
eb init -p python-3.9 aips
eb create aips-env
eb open
```

### Google Cloud Platform (App Engine)

1. Create `app.yaml`:
```yaml
runtime: python39
entrypoint: gunicorn -b :$PORT app:app

instance_class: F2

automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 10
```

2. Deploy:
```bash
gcloud app deploy
```

## Environment Variables

For production, consider using environment variables for configuration:

```python
# In app.py
import os

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'
```

Set them in your environment:
```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
```

## Nginx Reverse Proxy

For production with Nginx:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        alias /path/to/AGRICULTURAL-INTELLIGENCE-PREDICTION-SYSTEM/static;
    }
}
```

## SSL/HTTPS Setup

Use Let's Encrypt for free SSL certificates:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Performance Optimization

1. **Enable Caching**: Use Flask-Caching for response caching
2. **Use CDN**: Serve static files from a CDN
3. **Database**: Consider using a database for larger datasets
4. **Load Balancing**: Use multiple workers/instances for high traffic
5. **Monitoring**: Set up monitoring with tools like Prometheus or New Relic

## Security Considerations

1. **Change Debug Mode**: Set `DEBUG=False` in production
2. **Use HTTPS**: Always use SSL/TLS in production
3. **CSRF Protection**: Implement CSRF tokens for forms
4. **Input Validation**: Validate all user inputs
5. **Rate Limiting**: Implement rate limiting to prevent abuse
6. **Regular Updates**: Keep dependencies updated

## Monitoring and Logging

### Setup Logging
```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('aips.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('AIPS startup')
```

## Backup and Recovery

1. **Data Backup**: Regular backups of any databases or user data
2. **Version Control**: Keep code in Git
3. **Documentation**: Maintain deployment documentation
4. **Testing**: Test deployments in staging before production

## Troubleshooting

### Application won't start
- Check logs: `tail -f aips.log`
- Verify dependencies: `pip install -r requirements.txt`
- Check port availability: `lsof -i :5000`

### Performance issues
- Increase worker count in Gunicorn
- Enable caching
- Optimize database queries
- Use load balancer

### Memory issues
- Monitor memory usage: `top` or `htop`
- Adjust worker count
- Enable swap if needed
- Consider upgrading server resources

## Support

For deployment issues, please open an issue on GitHub or consult the documentation.
