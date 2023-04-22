import g


def requestPage(rKey, index):
    url = f"http://www.referenceusa.com/UsBusiness/Result/Page?requestKey={rKey}&pageIndex={index}"

    payload = f"requestKey={rKey}&sort=&direction=Ascending&pageIndex={index}&optionalColumn="
    headers = {
        'User-Agent': '',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain',
        'Cookie': ''
        }

    response = g.requests.request("GET", url, headers=headers, data=payload)

    soup = g.BeautifulSoup(response.text, 'html.parser')
    if index == 0:
        script = soup.find("script", string=lambda text: text and "var totalPages" in text)
        # Extract the JavaScript code
        javascript_code = script.string

        # Extract the value of the "totalPages" variable from the JavaScript code
        total_pages = None
        for line in javascript_code.splitlines():
            if 'var totalPages =' in line:
                total_pages = int(line.split('=')[1].strip().replace(';', ''))
                break
        return total_pages
    if index > 0:
        attr_list = soup.findAll(attrs="action-view-record")
        request_list = []
        for i in attr_list:
            r = i.previous_element.next_element.parent.contents[0].attrs['data-tagged-url'].rfind('recordId=')
            request_list.append(i.previous_element.next_element.parent.contents[0].attrs['data-tagged-url'][r+9:])
        return request_list
