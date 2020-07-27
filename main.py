test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  # create a stats dict
  stats = {}
  # Loop through our test entry 
  for log in logs:
    # parse out the individual pieces of the log entry
    log_parts = log.split(" ")
    
    # get the category 
    category = log_parts[0][1:-1]
    # get the http unicode
    http_code = log_parts[1]
    # get the http description
    start = log.find(http_code) + len(http_code) +1
    end = log.find(":")
    description = log[start:end]
    # get the error 
    error_text = log[end + 2:]
    
  # add the log entry to the multi-level dict
    if stats.get(category):
      if stats[category].get(http_code):
        if stats[category][http_code].get(description):
          if stats[category][http_code][description].get(error_text):
            stats[category][http_code][description][error_text] += 1
          else:
            stats[category][http_code][description][error_text] = 1
        else:
          stats[category][http_code][description] = { error_text: 1}
      else:
        stats[category][http_code] = { description: { error_text: 1}}
    else:
      stats[category] = { http_code: { description: { error_text: 1}}}
  return stats
    
print(log_stats(test_data))