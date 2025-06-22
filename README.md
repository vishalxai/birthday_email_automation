# Birthday Email Automation 🎂📧

A simple Python automation project that sends personalized birthday emails automatically.  
It reads birthday data from a CSV file, selects a random message template, and sends emails using SMTP.

---

## Features

✅ Reads birthdays from `birthdays.csv`  
✅ Sends automated birthday emails on matching dates  
✅ Picks a random letter template from `letter_templates/`  
✅ Uses `pandas` and `datetime` for data handling  
✅ Uses `smtplib` for email delivery  
✅ Fully customizable letter templates and CSV data  

---

## How it Works

1. Reads the current date (month & day)
2. Loads birthday data from `birthdays.csv`
3. If today matches any birthday:
    - Selects a random letter template
    - Replaces `[NAME]` with the person's name
    - Sends the email to the recipient

---

## Project Structure

```
birthday_email_automation/
│
├── birthdays.csv                # List of names, emails, and birth dates
├── letter_templates/            # Folder with letter_1.txt, letter_2.txt, letter_3.txt
│
└── main.py                      # Main Python script for automation
```

---

## Requirements

- Python 3.8+
- `pandas`
- `smtplib`
- Email account with App Password (Gmail / Outlook)

---

## Setup

1️⃣ Clone the repo:  
```bash
git clone https://github.com/your-username/birthday_email_automation.git
```

2️⃣ Install dependencies:  
```bash
pip install pandas
```

3️⃣ Enable App Passwords on your email account  
(Gmail: [Guide](https://myaccount.google.com/apppasswords))  

4️⃣ Add your email & app password in `main.py`

```python
my_email = "your_email@gmail.com"
password = "your_app_password"
```

5️⃣ Run the script manually, or schedule it to run daily (using cron / task scheduler)

---

## Example

```
name,email,year,month,day
mom,vishalxai@outlook.com,1971,06,21
dad,vishalxai@outlook.com,1966,08,16
```

---

## Author

Vishal Singh  
Follow my AI/ML journey 👉 [@vishalxai](https://twitter.com/vishalxai)

---

## License

MIT