#!/usr/bin/env python
# coding=utf-8


from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Chrome()

browser.get("http://localhost:8000")

assert "Django" in browser.title