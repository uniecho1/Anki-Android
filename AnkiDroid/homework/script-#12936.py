# coding: utf-8
#
import uiautomator2 as u2
import time


d = u2.connect()

d(resourceId="com.miui.home:id/icon_icon", description="AnkiDroid").click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/deck_name_linear_layout").long_click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/md_title", text="导出牌组").click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/md_button_positive").click()
time.sleep(1)
d(resourceId="com.ichi2.anki:id/md_button_negative").click()
time.sleep(1)
d.press("back")
time.sleep(1)
d.press("back")