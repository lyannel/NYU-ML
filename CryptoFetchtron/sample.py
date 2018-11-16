from SQL import db
from SQL.models import cryptodata,price


sample=cryptodata(coin="MEME_COIN")
# db.session.add(sample)
# db.session.commit()
#db.session.rollback() TO UNDO

#To print all
# use get(1) to get the ID
cd = cryptodata.query.all()
for fake_money in cryptodata:
	print(fake_money.coin)

ap=price(q=3,p=4,cid=sample)




#To delete all DATA
finalcd=cryptodata.query.all()
for bye in finalcd:
	db.session.delete(bye)

finalp=price.query.all()
for bye in price:
	db.session.delete(bye)

db.session.commit()