# Wishomatic

## Description
Wishomatic is a Python script that automates the process of sending personalized wishes via WhatsApp. The script takes a CSV file containing the date, phone number, and message (wish), and runs as a scheduled task (cron job) at 12 AM daily. It checks if there are any wishes for that day and automatically sends the corresponding wish to the specified phone number. 

## Tech Stack
![Image Alt](https://skillicons.dev/icons?i=py)

## How to run the project?

How to Run the Project?

1. Clone the Repository and Install Dependencies

- Clone the project repository to your local machine.
- Navigate to the project directory and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

2. Prepare the `data.csv` File

- Create a `data.csv` file in the same directory as the script.
- The CSV file should contain the following columns in the specified order:
  - Date (e.g., MM-DD)
  - Phone Number (e.g., +1234567890)
  - Wish (e.g., Happy Birthday!)
- Example CSV format:

```csv
date,phone_number,wish
03-21,+1234567890,Happy Birthday!
03-22,+0987654321,Happy Anniversary!
```

3. Set Up Cron Job to Run the Script

> [!NOTE]
> Make sure that your WhatsApp is logged in on your default browser

## Author
[Dev Shah](https://github.com/busycaesar)
