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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Cookie': '_ga_JMDCP9JFFY=GS1.1.1681780393.4.1.1681781046.0.0.0; _ga=GA1.1.188829893.1681436964; ai_user=hrg45hBKPHMrBM9zc0a575^|2023-04-14T01:51:44.936Z; _ga_Q1M017Q8EN=GS1.1.1681780449.10.1.1681781052.0.0.0; __utma=45961573.188829893.1681436964.1681698834.1681780450.10; __utmz=45961573.1681437107.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none); __hstc=63604784.62b2c95fa5f0493ab798448309f21b3a.1681437107548.1681780450082.1681781048178.11; hubspotutk=62b2c95fa5f0493ab798448309f21b3a; CurrentUser=56399; _gid=GA1.2.534202651.1681780394; BIGipServerrefusa_http=2639964352.20480.0000; __utmb=45961573.8.10.1681780450; ai_session=elLcevvJuKrhGd/m9Vka21^|1681780449782^|1681781053478; ln_or=eyIyOTcyNjYiOiJkIn0^%^3D; __hssc=63604784.2.1681781048178; _gat_UA-15188833-1=1; IIIV933375096=^#BEGMD5^#4ad82d8845dc5fff47552fe4646dfa3f^#ENDMD5^#0-he^|1774857^|45^|121^|0^|0; ASP.NET_SessionId=satqjdktsjpjilgloo0chvyw; .ASPXAUTH=82120C596306AE73F33633A4F66EF949BC60CCB5577741A7B2E534B52B6EC20B4E07644CAC034CACF8206A3E7C7531F40AF86D2BD225DE85E1CCCB282EB8328B4AB99366D963600D9BC71AC7D1069C6BA60C20DC85A6DE2B8744152B4D9C125CD8D32B36EBD2991FF8528B53A35C26B1682885DC09AAB8197F64E569C3FEE8FA3416745DC093C8097B2623FF8CA3446236A16F30D8899175D88A33957332856704D30B1AC05F8F5A38773A150585D7C6EBC04FD3B0D41CAF2BF1EEA9227918879537CD8075AF11836C2729833D8CB068BABFEEA09C43A339DBD1DAAC28753FF12F3F3D38FCE619F6601DEA8A410BC7112B309D93878E1205F118F408E74104EBF49DC396957F9E4056598B110E2997C7C1BD87DFFF0F6DA1A567C05390A5D91E540C4645FAA6E2924124398673F6B9A82F119D223734D440F76D440D147A109AF2644FCE7F6D154C1D76F07DAFB33D988AD8EF915EAF83FF1F9E822FA881BC1AA8DF173F27780D9173CB212446A0EC4DAA48AF4C10F320DF37FF2F514EE332F555E81A6B3EFCB6231FC5FDA9A2BD5F3C72E9F95B19F05B5979700986D5E14FD8D441CD8FE4A02277A13EF8411CCC578A31B4059681E5A9D0EC4B4653D54C94B495645385B29DD0ABD1D5E3D2454C80A540583B1D2D5EC8E67BEB997B1185524218457BCCD84FE7133D86FE123BD1D875D068D276A44775A475A5A6BA21F92740378B6134FC58730E62429F3CEC081CD29C5FAA371ACA7DBD82A5B101A8E76052BDF86868A22550A3; UserAuthenticated=true; TS0180d824=01065b9f508cb8b42559bdb205e99299a46ecd43150aff97b742d9b4c0e203b65e07f14c793bbdacf011bde5c7e0d2bfbe32fa5baf; isUsBusHistoricalTab=false; __utmc=45961573; __hssrc=1; __utmt=1; TS0180d824_77=08cfd42f6fab2800882261f6ae0051d48e6a904e07a20c54e8691eaaf3f7e5f1f3b19d7beeea4f3a6cb851454c2b6bbe087eb236c0824000c37265e6f6f51fb1a0507aee086cd568be55cb693d0d1ea03637215b57313eb20039247c38c2326d349d7ecdcc2d58947e374ac8ceef41da8ddf66e6e7414bec; .ASPXAUTH=BD352DD39798BACF91C8E522C43901BF2386957E946DAFC0C287A3903AE46578D7A2B535B9CD04F4049A1A659D70E99AE3CB0E9EFF5C5474CA0C8483806AFE70C49119B37483930B455BB0AFAB586F394FDEC73BEA8717A705A8AE4088FCE2A2C3F71AA0890D66C8412023396CAAA1F913FFA0646CEF3DD49948CD17746D31E5A734434FDE16A41C8D8186476250393F7C0D988245590E2C0997A1FAA4FBF785BA6F32D9393C09523DDDD4D3EA9710589007037DC13610CE5818158E750FA7A0645CB3AD32746E7712B92CC1AC19A75A49E70F3205D5B0A31204649593E860AA235EFFC36E1C11F9F169CBC9DF23125C9E32B167B2595F05A38815E24FD19E3A55318C7B1142EE157CEE17E56C6E24B441A3B894F45D14A8E0CDEEE51AA06BB4C3506F23F4587672BE0C7D234B270CA987626E5F9D3E614264BC4649B3D6B8FAFADEEFB7312967811EA1366A3282AA1E2F2E29CBDD08EA2679DA82A5FC1DEC75BB88001413AE9DC467F3AFDBDFAF33745FBA46F62D6CBE116CE8A1310EC35DACA20D9D1435E779027346A18A1A091E849D902226EE8FE7942AC54A1D0E35C56CA7EEEDF959E0BAA57B66F1AE2BCF2D488F773E23D42B7D408D2F0C84D550756303CA2B6373E910446CB18AFB45CBF36D8C4DA8EC8297ADF57F41990EE69E670E677547AEBC34415026E5A6659589716A1EA8E90F4FA14D37332546B01046EFC8903DF3EB3D9C64FAEF7B7BDCBB0224D7CB12C83122C63226B201EE20971AF6F840A852BA3AD4E70E1366B2252F03B40A; ASP.NET_SessionId=bpfle3xgn21rylcbdrmxafai; BIGipServerrefusa_http=2639964352.20480.0000; TS0180d824=01065b9f50cb63970603b46c8c33594e55babf70a754a5665d85826bec24c023268f2ffa31c6ef8d4ce66553e3e7517fe709a1c925; UserAuthenticated=true'
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
            print(err)
            g.ebo *= g.ebo
            print(g.ebo)
            print(i)
            g.sleep(g.ebo)
        except (g.requests.Timeout, TypeError, KeyError, IndexError) as err:
            print(err)
            print(i)
            g.sleep(g.st)
    return bList
