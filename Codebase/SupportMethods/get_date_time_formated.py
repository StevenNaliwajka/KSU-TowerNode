from datetime import datetime

def get_date_time_formated() -> str:
    # Get current date and time
    now = datetime.now()

    # Format as "month-day-year-hour-minute"
    formatted_time = now.strftime("%m-%d-%Y_%H_%M")

    return formatted_time