# data types in Python

from pyscript import display, document

# hours
has_delivery = True # boolean
business_hours = '7:00 am - 8:00pm'  # string

#hours
display(f"⏰ Opening Hours: {business_hours}", target="hours")

# delivery: Boolean
if has_delivery:
    display("Delivery Available 🎂", target="hours")
else:
    display("Delivery Not Available 🍰", target="hours")
