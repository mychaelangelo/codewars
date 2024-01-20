import time

def make_readable(seconds):
    hrs = seconds // 3600
    mins = (seconds - (hrs * 60 * 60)) // 60
    secs = (seconds - (hrs * 60 * 60)) - (mins * 60)
    output = [str(item) if len(str(item)) == 2 else "0"+ str(item) for item in [hrs,mins,secs]]
    return ":".join(output)


