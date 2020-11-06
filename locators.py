from appium import webdriver
from time import sleep


desired_cap = {
    "deviceName": "DeviceName",  # Paste the device name found from the Command Prompt inside the quotes here
    "platformName": "Android",
    "appPackage": "com.linkedin.android",
    "appActivity": "com.linkedin.android.authenticator.LaunchActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

sleep(5)

try:
    driver.find_element_by_id('com.linkedin.android:id/growth_prereg_fragment_account_exists').click()
    sleep(5)
except:
    print("n")
    sleep(5)

driver.find_element_by_id('com.linkedin.android:id/growth_login_join_fragment_email_address')
driver.find_element_by_id('com.linkedin.android:id/growth_login_join_fragment_email_address').send_keys('shubhamsharma112sjsj@gmail.com')
driver.find_element_by_id('com.linkedin.android:id/growth_login_join_fragment_password').send_keys('shubhamsharma112@link#1')
driver.find_element_by_id('com.linkedin.android:id/growth_login_fragment_sign_in').click()
sleep(5)

try:
    driver.find_element_by_id('com.linkedin.android:id/feed_interest_education_overlay')
    driver.find_element_by_id('com.linkedin.android:id/feed_interest_education_overlay').click()
except:
    print("n")

driver.find_element_by_xpath("//android.widget.TextView[@text='My Network']").click()
sleep(5)

driver.find_element_by_id('com.linkedin.android:id/mynetwork_cohort_see_more_title').click()
sleep(5)

driver.swipe(start_x=540, start_y=500, end_x=540, end_y=380)

elem_list = []

for i in range(500):
    new_elem = driver.find_elements_by_xpath("//android.widget.LinearLayout[@content-desc='Connect']")
    for j in new_elem:
        elem_list.append(j)
        status = j.get_attribute("content-desc")
        if status == "Connect":
            j.click()
    driver.swipe(start_x=530, start_y=1050, end_x=530, end_y=323)
    sleep(3)

print("Number of requests sent : ")
print(len(elem_list))
