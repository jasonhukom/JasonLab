from datetime import datetime, timedelta
from src.database import get_last_attendance, save_attendance

SCHOOL_START = "07:30" # To capture late student (30 minutes tolerance)
MIN_INTERVAL_MINUTES = 5

def process_attendance(user_id):
	now = datetime.now()
	today = now.date()
	time_format_second = "%H:%M:%S"
	time_format_minute = "%H:%M"

	last = get_last_attendance(user_id, today)

	# Avoid Duplicates
	if last:
		last_time = datetime.strptime(last["time"], time_format_second)
		differences = now - last_time
		if differences < timedelta(minutes=MIN_INTERVAL_MINUTES):
			return "BLOCKED", "Too fast"

		# if variabel Last status IN, now status is OUT logic (afterschool)
		if last["status"] == "IN":
			status = "OUT"
			note = "LEAVE"
		else:
			status = "IN"
			note = "LEAVE"
	else:
		# first scan today
		status = "IN"

		start_time = datetime.strptime(SCHOOL_START, time_format_minute).time()
		if now.time() > start_time:
			note = "LATE"
		else:
			note = "ON_TIME"

	save_attendance(user_id, status, note)
	return status, note

if __name__ == "__main__":
	process_attendance(input())
