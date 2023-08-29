def get_n(days):
    """ Format the days later into string"""
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


def add_time(start, duration, day=False):
  time, period = start.split(" ")
  hours, mins = map(int, time.split(":"))
  add_hours, add_mins = map(int, duration.split(":"))
  period = period.strip().lower()
  
  new_hours = hours + add_hours
  new_mins = mins + add_mins
  
  n = 0 #days later
  WEEK_DAYS = [
      "monday",
      "tuesday",
      "wednesday",
      "thursday",
      "friday",
      "saturday",
      "sunday",
  ]
    # Shift minutes to hour if minutes is over 60
  if new_mins >= 60:
      new_hours += int(new_mins / 60)
      new_mins = int(new_mins % 60)

  if add_hours or add_mins:
      # If `PM`, flip period to `AM` if hours over 12
      if period == "pm" and new_hours > 12:
          # if hours over 24hr then add  days
          if new_hours % 24 >= 1.0:
              n += 1

      if new_hours >= 12:
          hours_left = new_hours / 24
          n += int(hours_left)

          # e.g: 54hr / 24 = 2.25 days <-- append 2 days
          # e.g.: 36hr / 24 = 1.5 days <-- append 1 days

      temp_hours = new_hours
      while True:
          # Constantly reverse period until
          # new_hours are less than half a day
          if temp_hours < 12:
              break
          if period == "am":
              period = "pm"
          else:
              period = "am"
          temp_hours -= 12

  """
  Recalculate Hours and Minutes 
  
   Since we have already taken care of the days,
   we now need to calculate the hours remaining.
   This can be done by subtracting the remaining days(in hours) 
   from the total hours remaining 
      
      e.g. hrs % oneday -->  55hrs % 24 = 7 ---> 7 hours remaining
  """
  remaining_hours = int(new_hours % 12) or hours + 1
  remaining_mins = int(new_mins % 60)

  # Format the results
  results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
  if day:  # add the day of the week
      day = day.strip().lower()
      selected_day = int((WEEK_DAYS.index(day) + n) % 7)
      current_day = WEEK_DAYS[selected_day]
      results += f", {current_day.title()} {get_n(n)}"

  else:  # add the days later
      results = " ".join((results, get_n(n)))

  return results.strip()