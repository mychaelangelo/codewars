def remove_url_anchor(url):
    if '#' in url:
        return url[:url.index('#')]
    else:
        return url


result_1 = remove_url_anchor("www.codewars.com#about") # -> "www.codewars.com"
result_2 = remove_url_anchor("www.codewars.com?page=1") # ->"www.codewars.com?page=1"

print(result_1)
print(result_2)
