from notifier.excel_reader import read_users, read_email_template
from notifier.email_sender import send_email
from notifier.validators import is_valid_email


def send_notifications(environment):
    """
    Send UAT or PROD notification emails.
    """

    environment = environment.upper()

    # Validate environment
    if environment not in ["UAT", "PROD"]:
        raise ValueError("Environment must be either 'UAT' or 'PROD'.")

    # Select Excel sheet
    sheet = "UATUser" if environment == "UAT" else "ProdUser"

    print("=" * 55)
    print(f"Environment : {environment}")
    print(f"Reading users from '{sheet}' sheet...")
    print("=" * 55)

    # Read users and email template
    users = read_users(sheet)
    subject, body = read_email_template(environment)

    success_count = 0
    failed_count = 0

    # Send emails
    for _, user in users.iterrows():

        name = str(user["Name"]).strip()
        email = str(user["Email"]).strip()

        # Validate email format
        if not is_valid_email(email):
            print(f"✗ Invalid email format : {email}")
            failed_count += 1
            continue

        # Personalize email
        personalized_body = body.replace("[Name]", name)

        try:
            send_email(
                subject,
                personalized_body,
                email
            )

            print(f"✓ Email sent to {email}")
            success_count += 1

        except Exception as e:
            print(f"✗ Failed to send email to {email}")
            print(f"  Error : {e}")
            failed_count += 1

    # Summary
    print("\n" + "=" * 55)
    print("Notification Summary")
    print("=" * 55)
    print(f"Environment        : {environment}")
    print(f"Total Active Users : {len(users)}")
    print(f"Emails Sent        : {success_count}")
    print(f"Failed             : {failed_count}")
    print("=" * 55)