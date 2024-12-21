

## Overview

This script monitors the expiration status of SSL certificates for a list of hostnames and sends email alerts based on the remaining validity period. Alerts are categorized into different severity levels depending on the number of days left before expiration.

## Features

- Checks SSL certificate expiration dates for a list of hostnames.
- Sends email alerts to notify about the certificate status:
    - **Information:** Certificate expiry is more than 30 days away.
    - **Warning:** Certificate expiry is between 15 to 30 days.
    - **Critical Warning:** Certificate expiry is between 10 to 15 days.
    - **Error:** Certificate expiry is less than 10 days or if an issue occurs during verification.

## Requirements

- Python 3.x
- Required libraries:
    - `certifi`
    - `ssl`
    - `socket`
    - `cryptography`
    - `smtplib`
    - `datetime`

You can install the required libraries using `pip`:

```bash
pip install certifi cryptography
```

## Configuration

1. **Email Settings**  
    Modify the following variables in the `send_email` function:
    
    - `smtp_server`: SMTP server address.
    - `sender_email`: Your email address for sending alerts.
    - `receiver_email`: A list of email addresses to receive alerts.
    - `password`: Your email account's password.
2. **Hostname List**  
    Replace the `hn` variable with a list of hostnames to monitor, separated by commas:
    
    ```python
    hn = ["example.com", "anotherdomain.com"]
    ```
    

## Usage

1. Run the script:
    
    ```bash
    python ssl_monitor.py
    ```
    
2. The script will:
    
    - Check the SSL certificate for each hostname.
    - Calculate the remaining validity period.
    - Send an appropriate email alert based on the days left before expiration.

## Error Handling

If an error occurs during SSL verification, an email is sent with the error details for troubleshooting.

## Example Email Alerts

- **Subject:** `SSL Certificate Status for example.com` **Body:** `SSL certificate expiration date for example.com is going to expire in 40 days.`
    
- **Subject:** `SSL Certificate Warning for example.com` **Body:** `SSL certificate expiration date for example.com is going to expire in 20 days.`
    
- **Subject:** `SSL Certificate Error for example.com` **Body:** `SSL certificate expiration date for example.com is going to expire in 5 days.`
    

## Notes

- Ensure that the sender email account allows less secure app access or use an app-specific password if needed.
- Test the email configuration before deploying the script to ensure alert delivery.

This script provides a basic SSL certificate monitoring solution and can be extended for additional features, such as logging and integration with notification systems.
