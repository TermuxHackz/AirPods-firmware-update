from datetime import datetime
import pytz

def format_multi_timezone(dt=None):
    """
    Format the given datetime or current time for multiple major timezones.
    
    Args:
    dt (datetime, optional): The datetime to format. If None, uses current time.
    
    Returns:
    str: Formatted datetime string for multiple timezones.
    """
    if dt is None:
        dt = datetime.now(pytz.utc)
    elif dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    
    timezones = [
        ('US/Pacific', 'PT'),
        ('US/Eastern', 'ET'),
        ('Europe/London', 'GMT'),
        ('Europe/Berlin', 'CET'),
        ('Asia/Tokyo', 'JST'),
    ]
    
    formatted_times = []
    for tz_name, tz_abbr in timezones:
        tz = pytz.timezone(tz_name)
        local_time = dt.astimezone(tz)
        formatted_times.append(f"{local_time.strftime('%I:%M %p')} {tz_abbr}")
    
    return ' | '.join(formatted_times)

def format_pacific_time(dt=None):
    """
    Format the given datetime or current time to Pacific Time.
    
    Args:
    dt (datetime, optional): The datetime to format. If None, uses current time.
    
    Returns:
    str: Formatted datetime string in Pacific Time.
    """
    pacific_tz = pytz.timezone('US/Pacific')
    
    if dt is None:
        dt = datetime.now(pytz.utc)
    elif dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    
    pacific_time = dt.astimezone(pacific_tz)
    return pacific_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")