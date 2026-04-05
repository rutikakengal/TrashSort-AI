FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run inference by default
CMD ["python", "inference.py"]