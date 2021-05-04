from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.message import EmailMessage

#### Email Info ####
# TODO: Update your email, password and recipient
my_email = "INSERT YOUR EMAIL"
# Don't let anyone see your password!
password = "INSERT YOUR PASSWORD"
recipient = "INSERT THE EMAIL YOU'RE SENDING IT TO"

# headers that the amazon webpage needs
headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
	"Accept-Language" : "en-US,en;q=0.5"
}

# Getting the amazon website using the request library
response = requests.get("https://www.amazon.com.mx/Aud%C3%ADfonos-inal%C3%A1mbricos-QuietComfort-Amazon-integrada/dp/B0756CYWWD/ref=sr_1_5?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=noise+cancelling+headphones&qid=1620086893&sr=8-5"
						, headers = headers)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, 'lxml')
product = soup.title.string[0:68]

price = soup.select_one(selector="#priceblock_dealprice").string
price = price[1:6]
price = price.replace(",", "")
price = int(price)

def product_price_print():
	print(f"The product is: {product}. This product costs {price}. THEY ARE REAL CHEAP, BUY THEM!")

product_price_print()

the_product_is_cheaper = True
iterations = 0

while the_product_is_cheaper:
	time.sleep(0)
	minute = 0
	iteration = 0

	# If the target of the product is less than 4000, then It'll send the message
	if the_product_is_cheaper == True and product <= 4000:

		#Sending the message
		subject = f"{product} are on {price}!!!"
		body = f"\n\n{product_price_print()}\n\n Your python bot (:"

		# build-up email details using email.message module
		message = EmailMessage()
		message["Subject"] = subject
		message["From"] = my_email
		message["To"] = recipient
		message.set_content(body)

		# send the message via smtp using details above
		with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
			connection.starttls()
			connection.login(my_email, password=password)
			connection.send_message(message)

		the_product_is_cheaper = False