import smtplib,random,pandas
import datetime as dt

smtplib.SMTP('smtp.gmail.com', port=587)
mymail = 'aditesseracat@gmail.com'
pwd = 'lirl htyj hqzv hlxg'

now = dt.datetime.now()

def send(i,txt):
    with smtplib.SMTP('smtp.gmail.com')as cnc:
        cnc.starttls()
        cnc.login(user=mymail,password=pwd)
        cnc.sendmail(
            from_addr=mymail,
            to_addrs=i,
            msg=f"Subject:Birthday Birthday Birthday{txt}"
        )

with open("birthdays.csv", 'r') as b, open("letter_1.txt") as f:
    msg = random.choice(f.read().split("-"))
    print(msg)
    data = pandas.read_csv(b).to_dict(orient="records")
    for i in data:
        print(i)
        if now.year == i["year"] and now.month == i["month"] and now.day == i["day"]:
            msg = msg.replace("[NAME]", i["name"])
            send(i["email"],msg)
