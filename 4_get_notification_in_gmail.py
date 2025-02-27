import xlwings as xw
import smtplib
import time

# Email Configurations
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "07navneet@gmail.com"
SENDER_PASSWORD = "zedg dfht tmcn dvru" # app password set in gmail
RECIPIENT_EMAIL = "navneet7988@gmail.com"

# Excel Monitoring Configurations
EXCEL_FILE_PATH = r"C:\Users\07nav\Downloads\upstoxbaji2\Bonds Live-macro.xlsm"
SHEET_NAME = "Sheet4"
MONITOR_CELL = "K4"
THRESHOLD_VALUE = 500  # Set your limit

def send_email(current_value):
    # """Send an email alert when the threshold is crossed."""
    subject = "Threshold Alert!"
    body = f"Alert: The monitored value {current_value} has crossed the limit {THRESHOLD_VALUE}."
    
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor_excel():
    # """Continuously monitor the Excel file for value changes."""
    app = xw.App(visible=False)  # Run Excel in the background
    wb = xw.Book(EXCEL_FILE_PATH)  # Connect to the open workbook
    ws = wb.sheets[SHEET_NAME]

    while True:
        try:
            current_value = ws.range(MONITOR_CELL).value  # Read cell value
            
            if isinstance(current_value, (int, float)) and current_value > THRESHOLD_VALUE:
                send_email(current_value)
            
            time.sleep(60)  # Wait for 5 minutes before checking again
            
        except Exception as e:
            print(f"Error reading Excel: {e}")

if __name__ == "__main__":
    monitor_excel()
