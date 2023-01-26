import pytest
import requests
import json
import os
import urllib.request
url = "https://sspdev.okko.ua/login"


def test_check_ping():
  hostname = url
  response = os.system("ping -c 1 " + hostname)
  # and then check the response...
  if response == 0:
    pingstatus = "Network Active"
  else:
    pingstatus = "Network Error"
  with open("response_ping.json", "w") as f:
    json.dump(pingstatus, f, sort_keys=True, indent=4)
  return pingstatus


def test_check_google_ping():
  hostname = "google.com.ua"
  response = os.system("ping -c 1 " + hostname)
  # and then check the response...
  if response == 0:
    pingstatus = "Network Active"
  else:
    pingstatus = "Network Error"
  with open("response_ping.json", "a+") as f:
    f.seek(0, os.SEEK_END)
    json.dump(pingstatus, f, sort_keys=True, indent=4)
  return pingstatus


def test_check_stackoverflov_status():
  response = urllib.request.urlopen("https://www.stackoverflow.com").getcode()
  with open("response_ping.json", "a+") as f:
    f.seek(0, os.SEEK_END)
    json.dump(response, f, sort_keys=True, indent=4)
  assert response.status_code ==200
  return response