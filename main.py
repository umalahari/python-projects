import send_single_email
import send_bulk_emails


# main start 
if __name__ == "__main__":
    print("Select type emails send\n 1. Single email send \n 2. Bulu email send")
    choice = int(input("Please select your type of email send: "))
    subject = input("Enter subject of an email: ")
    body = input("Enter body of an email: ")
    if choice == 1:
        reciver_email = input("Enter reciver email: ")
        # send single email function call
        send_single_email.single_sender(
            to_email= reciver_email,
            subject = subject,
            body= body
        )
    elif choice == 2:
        reciver_email_list = list(input("Enter all emails sperated by comma: ").split(","))
        # send bulk email  function call
        send_bulk_emails.send_bulk_emails(
            emails= reciver_email_list,
            subject= subject,
            body= body
        )