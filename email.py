import emails
message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                          subject="Your receipt No. 567098123",
                          mail_from=('Some Store', 'store@somestore.com'))
message.attach(data=open('bill.pdf'), filename='bill.pdf')

r = message.send(to='yohan.park@semifive.com', smtp={'host': 'aspmx.l.google.com', 'timeout': 5})
assert r.status_code == 250