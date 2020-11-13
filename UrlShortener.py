import pyshorteners

url=input("Enter the url:\n")
print("URL after shortening is : ",pyshorteners.Shortener().tinyurl.short(url))