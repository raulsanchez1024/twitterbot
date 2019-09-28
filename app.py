from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.bot = webdriver.Firefox(executable_path='/Users/raul/Downloads/geckodriver')

  def login(self):
    bot = self.bot
    bot.get('https://twitter.com')
    time.sleep(3)
    email = bot.find_element_by_class_name('email-input')
    password = bot.find_element_by_name('session[password]')
    email.clear()
    password.clear()
    email.send_keys(self.email)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)

  def like_tweet(self, hashtag):
    bot = self.bot
    bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
    time.sleep(3)
    for i in range(1,3):
      bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
      time.sleep(2)
      links = [i.get_attribute('href')
                for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
      for link in links:
        bot.get(link)
        try:
          time.sleep(5)
          bot.find_element_by_xpath("//div[@aria-label='Like']").click()
          time.sleep(10)
        except Exception as ex:
          print('Something went wrong')



tb = TwitterBot('<email/username>', '<password>')
tb.login()
tb.like_tweet('<hashtag>')
