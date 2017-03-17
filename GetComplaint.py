import datetime
import csv
#"2052"
import requests as req
cookie = dict(cookies_are=open('WaveCookie.txt','r').read())
ListUrl = 'https://wave.xiaojukeji.com/v2/dc/driverdiagnosis/driverlist'
ComplaintUrl='http://wave.xiaojukeji.com/v2/dc/ordercomplaint/orderlist'
r = req.get(ListUrl,params={'size':'100','model':'5'},cookies = cookie)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.202 Safari/537.36',
'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate'}
data = r.json()['data']['data']
with open(datetime.datetime.now().strftime('20%y-%m-%d')+'Complaint.csv','w',newline='') as f:
	fieldnames=['姓名','订单ID','团队','星级']
	w = csv.DictWriter(f,fieldnames=fieldnames)
	for d in data:
		ComplaintJson = req.get(ComplaintUrl,cookies=cookie,params={'star':'1','order_type':'2','comment':'1','driver_id':d['driver_id']})
		Count = ComplaintJson.json()['data']['count']
		if Count == '0':
			continue
		else:
			CData =ComplaintJson.json()['data']['data']
			for c in CData:
				w.writerow({'姓名':c['name'],'订单ID':c['order_id'],'团队':c['org_name'],'星级':c['star']})
	for d in data:
		ComplaintJson = req.get(ComplaintUrl,cookies=cookie,params={'star':'2','order_type':'2','comment':'1','driver_id':d['driver_id']})
		Count = ComplaintJson.json()['data']['count']
		if Count == '0':
			continue
		else:
			CData =ComplaintJson.json()['data']['data']
			for c in CData:
				w.writerow({'姓名':c['name'],'订单ID':c['order_id'],'团队':c['org_name'],'星级':c['star']})