def domain_name(url):

    if url.startswith("http://"):
        url = url[len("http://"):]
    elif url.startswith("https://"):
        url = url[len("https://"):]
    
    if url.startswith("www."):
        url = url[len("www."):]

    dot_index = url.find(".")

    if dot_index != -1:
        return url[:dot_index]
    else:
        return url

print (domain_name("https://www.bing.com/videos"))
print (domain_name("http://google.com"))
print (domain_name("https://youtube.com"))
print (domain_name("www.otto.de"))