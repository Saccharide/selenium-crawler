from selenium import webdriver

# Open up a Firefox Web page (if left empty, it will look from /usr/bin)
driver = webdriver.Firefox()
# driver.get("http://thingsthataresmart.wiki/index.php?title=ThingsThatAreSmart_Wiki")

## Unpublished SmartApps
#driver.get("http://thingsthataresmart.wiki/index.php?title=Category:Unpublished_SmartApps")
driver.get("https://github.com/Saccharide/ifttt_crawler")
driver.maximize_window()
# element = driver.find_element_by_tag_name('body')
element = driver.find_element_by_id('readme')
element_png = element.screenshot_as_png
with open("test2.png", "wb") as file:
    file.write(element_png)
# driver.get_screenshot_as_file("test.png")
driver.close()
# Extract list of links from the SmartThings Forum

