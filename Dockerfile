FROM python:3.13.3

# Install OpenVPN, curl, and other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openvpn curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Copy your application code (assuming you have a Python app)
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose necessary ports if applicable
EXPOSE 8080

# Command to run your app (adjust based on your app)
CMD ["python", "bot.py"]
