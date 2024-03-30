
price_url="https://finnhub.io/api/v1/quote"
params={
    "symbol":"NVDA",
    "token":"asd"
}
import requests,smtplib
my_mail="asd@gmail.com"
to_mail="asd@gmail.com"
password="password"

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(from_addr=my_mail,to_addrs=to_mail,msg=f"Subject:Nvidia Alert!\n\n{whole_new}")



respond=requests.get(price_url,params=params)
respond.raise_for_status()
data=respond.json()

yesterday_close_price=float(data["pc"])
current_price=float(data["c"])
diff=abs(yesterday_close_price-current_price)
percentage_difference = (diff / yesterday_close_price) * 100



if percentage_difference > 5:

    api_key="asd"
    url="https://newsapi.org/v2/top-headlines"
    parameters={
        "q":"nvidia",
        "apiKey":api_key
    }
    respond=requests.get(url,parameters)
    respond.raise_for_status()
    news_data=respond.json()["articles"]
    news_list=[]
    whole_new=""
    for i in range(len(news_data)):
        news_list.append(news_data[i]["description"])
    for i in range(len(news_list)):
        whole_new+=f"{i + 1}-{news_list[i]}"
        whole_new+="\n\n"
    whole_new.encode("utf-8")
    send_mail()





