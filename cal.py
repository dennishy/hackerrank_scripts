import calendar as c

mm,dd,yyyy = [int(x) for x in input().split()]

out = c.day_name[c.weekday(yyyy,mm,dd)]

print(out.upper())

