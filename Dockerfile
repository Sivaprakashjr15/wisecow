# Use a lightweight Linux base image
FROM debian:bullseye

# Set environment variables
ENV SRVPORT=4499

# Install prerequisites
RUN apt-get update && \
    apt-get install -y cowsay fortune netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the wisecow.sh script
COPY wisecow.sh /app/wisecow.sh

# Set script as executable
RUN chmod +x /app/wisecow.sh

# Set working directory
WORKDIR /app

# Expose the application's port
EXPOSE 4499

# Run the script
CMD ["./wisecow.sh"]
