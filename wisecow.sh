#!/usr/bin/env bash

# Configuration
SRVPORT=4499
RSPFILE=response
LOGFILE=wisecow.log

# Clear old response and log files
rm -f $RSPFILE
rm -f $LOGFILE
mkfifo $RSPFILE

# Function to log messages
log_message() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" | tee -a $LOGFILE
}

get_api() {
    read line
    log_message "Received request: $line"
    echo $line
}

handleRequest() {
    # Process the request
    get_api
    mod=$(fortune)
    log_message "Generated fortune: $mod"

cat <<EOF > $RSPFILE
HTTP/1.1 200 OK

<pre>$(cowsay "$mod")</pre>
EOF
    log_message "Response sent."
}

prerequisites() {
    command -v cowsay >/dev/null 2>&1 &&
    command -v fortune >/dev/null 2>&1 || {
        log_message "Prerequisites missing: cowsay or fortune not found."
        echo "Install prerequisites."
        exit 1
    }
    log_message "Prerequisites verified."
}

main() {
    prerequisites
    log_message "Starting Wisecow server on port $SRVPORT..."

    while true; do
        cat $RSPFILE | nc -lN $SRVPORT | handleRequest
        sleep 0.01
    done
}

main
