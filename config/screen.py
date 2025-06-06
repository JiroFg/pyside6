from screeninfo import get_monitors, Monitor

def get_monitor_size() -> Monitor:
    monitors = get_monitors()
    return monitors[0]