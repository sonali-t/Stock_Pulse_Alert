from selenium import webdriver
import time
import yagmail


def initiate_driver():
  # options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver
  
# extracting stock drop percentage
def extract_text(text):
  drop_value = float(text.split(" ")[0])
  return drop_value

def email_content(drop_value):
  # as a security measure use credentials store as a environment variables 
  sender = 'user46018@gmail.com'
  receiver = 'senders@gamil.com'
  subject = "Stock Trend Drop!!"
  password = "nknzq629"
  contents = """
  The stock price trend is below -0.10%. It has dropped to {drop_value}%!
  """

  yag = yagmail.SMTP(user=sender, password=password)
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")

  
def main():
  driver = initiate_driver()
  time.sleep(2)
  trend_drop_element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')

  trend_drop_text = extract_text(trend_drop_element.text)
  
  # if(trend_drop_text < -0.10):
  email_content(trend_drop_text)
  print(trend_drop_text)
  
main()
