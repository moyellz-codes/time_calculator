def add_time(*args):
  time = list(args)
  timecode = time[0][-2:]
    
  Days_of_Week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  Days_of_week_lower = []

  #input time
  input_hr = time[0][:2]
  if ":" in input_hr:
    input_hr = int(input_hr[0])
  else:
    input_hr = int(time[0][:2])
  
  input_min = int(time[0][-5:-2])

  #Duration Time
  duration_hour = time[1]
  y = len(duration_hour) - 3
  duration_hour = int(duration_hour[:y])
  duration_min = int(time[1][-2:])
  #24 hr clock converter: convert 12hr clock to 24 hr clock
  if timecode == "AM":
    t4_time = ((input_hr*100)+input_min)
  else:
    t4_time = ((input_hr*100)+1200)+input_min

  #time calculator
  if len(str(t4_time)) == 3:
    t4hr = int(str(t4_time)[0])
    t4min = int(str(t4_time)[-2:])
  else:
    t4hr = int(str(t4_time)[:2])
    t4min = int(str(t4_time)[2:])

  #convert hrs into mins
  new_time = ((1440*(t4hr + duration_hour))/24)+(t4min)+(duration_min)

  #number of days
  no_days = new_time // 1440

  #convert back into a 24hr clock
  final_min = (t4min + duration_min)%60
  final_hr = t4hr + duration_hour + ((t4min+duration_min)//60)

  y = final_hr//12
  z = y % 2

  
  #Timecode
  if final_hr > 11 and z != 0:
    tcode = "PM"
  else:
    tcode = "AM"

  #Converting result into 12 hr clock
  if final_hr <=11:
    thr = final_hr
  if final_hr == 12:
    thr = 12
  if final_hr > 12:
    thr = final_hr%12

  if thr == 0:
        thr = 12
  else:
    thr = thr

  if len(str(final_min))<2:
    tmin = "0"+str(final_min)
  else:
    tmin=str(final_min)

  #Determining the day of the week

  for i in Days_of_Week:
    Days_of_week_lower.append(i.lower())

  if len(time) == 3:
    Day = time[2]
    Day = Day.lower()
    n = len(Days_of_week_lower)
    x = no_days
    position = Days_of_week_lower.index(Day)
    
    pos_locator = position +1 + x

    if pos_locator <= n:
      pos_locator = pos_locator -1
        
    elif pos_locator % 7 == 0:
      pos_locator = 6

    else:
      pos_locator = (pos_locator % 7) -1

    day_of_week_text = Days_of_Week[int(pos_locator)]
    
    #stating the number of days: future Day text
  if no_days < 1:
    f_day = ""
  elif no_days < 2 and no_days >= 1:
    f_day = " (next day)"
  else:
    f_day = str(" (")+str(int(int(no_days)))+(" days later)")

  #returning reuslts
  if len(time) == 3:
    Result = str(int(thr))+":"+tmin+" "+str(tcode)+", "+str(day_of_week_text)+f_day
    return Result
  else:
    Result = str(int(thr))+":"+tmin+" "+str(tcode)+f_day
    return Result
