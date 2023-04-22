import g
import random


def requestDetails(rList, rKey, busObj):
    while 1:
        try:
            bList = []
            for i in rList:
                url = f"http://www.referenceusa.com/UsBusiness/Detail/Tagged/{rKey}?recordId={i}"

                payload = {}
                headers = {
                    'User-Agent': '',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Cookie': ''
                }

                response = g.requests.request("GET", url, headers=headers, data=payload)
                soup = g.BeautifulSoup(response.text, 'html.parser')

                d = soup.find(class_="load-on-visible").attrs
                busObj.companyName = d['data-name']
                busObj.address = d['data-thoroughfare']
                busObj.city = d['data-city']
                busObj.state = d['data-administrative-area']
                busObj.zip = d['data-postal']
                busObj.phone = d['data-phone']
                busObj.recordId = i

                # find the tag element with text content
                th = soup.select_one('th:-soup-contains("SIC Code")')
                if th is not None:
                    busObj.sic = th.parent.find_next_sibling().contents[1].next.text

                th = soup.select_one('th:-soup-contains("NAICS Code")')
                if th is not None:
                    busObj.naics = th.parent.find_next_sibling().contents[1].next.text

                th = soup.select_one('th:-soup-contains("IUSA Number")')
                if th is not None:
                    busObj.iusa = th.find_next_sibling().text.strip()

                th = soup.select_one('th:-soup-contains("Credit Rating")')
                if th is not None:
                    busObj.cs = th.find_next_sibling().text.strip()

                emp = soup.select_one('caption:-soup-contains("Business Demograph")').find_next('td').text.strip()
                empl = emp.split('-')
                print(empl)
                try:
                    busObj.empMin = empl[0]
                    busObj.empMax = empl[1]
                except:
                    busObj.empMax = emp
                    busObj.empMin = emp
                busObj.recordType = 'verified'
                if soup.find(class_='VerifiedRecord') is None:
                    busObj.recordType = 'unverified'

                busObj.fax = soup.find(id='fax').find_next_sibling().text.strip()
                busObj.execName = soup.select_one('caption:-soup-contains("Management Directory")').find_next('td').text.strip()
                busObj.execTit = soup.select_one('caption:-soup-contains("Management Directory")').find_next('td').find_next('td').text.strip()

                bList.append(busObj)
                busObj = g.Bus()
                print(f'{len(bList)}/{len(rList)}')
                g.sleep(g.st * random.uniform(1.3, 1.9))
            break
        except AttributeError as err:
            # Attribute Error typically from Captcha page, use exponential back off.
            print(err)
            epo = g.ebo
            g.ebo *= epo
            print(g.ebo)
            print(i)
            print("You have fucked up somewhere")
            g.sleep(g.ebo)
        except (g.requests.Timeout, TypeError, KeyError, IndexError) as err:
            print(err)
            print(i)
            g.sleep(g.st)
    return bList
