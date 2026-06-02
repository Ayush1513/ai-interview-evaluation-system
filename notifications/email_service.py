import smtplib
from email.message import EmailMessage


def send_report_email(
    hr_email,
    report_path,
    final_score,
    recommendation
):

    sender_email = "yourgmail@gmail.com"
    app_password = "your_app_password"

    msg = EmailMessage()

    msg["Subject"] = "Interview Report Generated"
    msg["From"] = sender_email
    msg["To"] = hr_email

    msg.set_content(
        f"""
Interview Evaluation Completed

Final Score: {final_score}/10

Recommendation: {recommendation}

The report is attached.
"""
    )

    with open(report_path, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="pdf",
            filename="candidate_report.pdf"
        )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            app_password
        )

        smtp.send_message(msg)

    print("HR notification sent")