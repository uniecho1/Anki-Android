# coding: utf-8
#
import uiautomator2 as u2
import time


d = u2.connect()

d(resourceId="com.miui.home:id/icon_icon", description="AnkiDroid").click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/fab_main").click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/add_shared_action").click()
time.sleep(10)
d.click(0.192, 0.307)
time.sleep(10)
d.click(0.123, 0.53)
time.sleep(10)
d.click(0.115, 0.948)
time.sleep(3)
d.press("home")
time.sleep(2)
d.press("home")
d(resourceId="com.miui.home:id/icon_icon", description="AnkiDroid").click()

