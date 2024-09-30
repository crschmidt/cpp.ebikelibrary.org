import csv
import sys
from datetime import datetime


r = csv.reader(open(sys.argv[1]))
next(r)
test = []
for row in r:
    timestamp, _, share, can_share, name, _, purchase, purchase_bike, _ = row

    if can_share == "Yes":
        parsed_date = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        test.append([name, share, parsed_date])
test.reverse()
for i in test:
        print("""
<div class="testimonial">
        <div class="testimonial-author">%s</div>
%s
<div class="testimonial-date">%s</div>
</div>""" % (i[0], i[1], i[2].strftime("%B %d, %Y")))

