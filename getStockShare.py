import requests
from bs4 import BeautifulSoup
import csv

# string to number
def convertToNumber(val):

    if (type(val) == str):

        val = val.replace(',','')
        if(val.find('%') != -1 ):
            val = val.replace('%','')
            return float((val).replace('%','')) / 100
        if val.isdigit():
            return float(val)

    elif (type(val) == int or type(val) == float):
        return val
    else:
        return -1

def getStockHtml(url):
    res = requests.get(url)
    return res.text

def parserStockData(data):
    soup = BeautifulSoup(data,'html.parser')
    i = 0
    stock_list = []
    stock = {}
    for td in soup.select('#oMainTable td')[12:]:
        if not td.has_attr("colspan"):
            # print(td.text)
            val = (td.text).strip()
            i += 1
            if i == 1:
                stock['name'] = val
            if i == 2:
                stock['share'] = convertToNumber(val)
            if i == 3:
                stock['ratio'] = convertToNumber(val)
            if i == 4:
                stock['increase'] = convertToNumber(val)
                stock_list.append(stock)
                # print("=============================")
                # print(stock_list)
                i = 0
                stock = {}
        # print(stock)
    # print(stock_list)
    return stock_list


# url= "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC01-006001"
url_list = ["http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC01-006001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDS21-017017",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT02-018003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT03-018004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT04-018005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT07-018006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT09-018007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT12-018008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT11-018009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0017-018048",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKY17-018055",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT161-018093",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACYT162-018094",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS13-024001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS03-024002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS04-024003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS06-024004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS07-024005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS25-024020",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJS30-024025",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0025-028001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDF07-028003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDF14-028010",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTT03-037003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTT06-037006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTC01-037011",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTC10-037012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACSH03-037019",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACGC01-003001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACGC08-003003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACGC09-003004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACUS03-003012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACII02-020001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACII11-020005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0004-020006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACII03-020007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACII01-020016",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACII21-020023",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCB01-047001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDD01-005001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDD04-005003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACDD05-005004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACAP01-029002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACAP04-029004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACBR01-016001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML05-007002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML02-007003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML01-007004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML07-007005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML09-007007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML12-007008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACML14-007011",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACES10-038008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACAI01-041001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCY01-010001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCY03-010002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCY06-010004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCY07-010005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCY14-010013",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNC11-039005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNC13-039007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNC16-039008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNC38-039025",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0014-009001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS01-009002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS02-009003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS03-009004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS06-009005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS09-009006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS10-009007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS14-009008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACPS23-009012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC01-006001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC05-006003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC06-006004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACIC08-006006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKH03-006018",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKH05-006020",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKH07-006021",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKH19-006025",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0001-006034",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKH29-006035",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKG01-014001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACKG15-014013",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFP03-035008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFP04-035009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFP10-035011",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFP11-035012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCT01-035016",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0029-035020",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0015-035028",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFT01-004001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFT12-004013",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH01-031004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH03-031005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH06-031006",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH08-031007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH04-031008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH07-031009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH11-031011",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH13-031013",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFH15-031015",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCS02-019005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCS07-019008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCS09-019009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0013-008004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCH01-012001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCH03-012002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCI03-030003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCI07-030004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCI12-030005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCI05-030023",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0005-030025",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0021-021002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTS09-021005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTS10-021007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTS18-021009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA03-001001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0028-001002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA04-001003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA09-001004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA10-001005",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA13-001007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=AC0023-001008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA15-001009",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA17-001012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCA19-001015",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNB01-050001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACNB02-050002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACFE01-034001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJF87-032003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJF76-032004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJF83-032011",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJF51-032012",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACJF105-032031",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCF01-043001",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACUI03-022002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACUI08-022008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACTI02-002002",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCP03-026003",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCP04-026004",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCP07-026007",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCP10-026008",
            "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACCP15-026010"
            ]
exclude_stock = [
    "彰化銀",
    "京城銀",
    "台中銀",
    "臺企銀",
    "高雄銀",
    "聯邦銀",
    "遠東銀",
    "安泰銀",
    "華南金",
    "富邦金",
    "國泰金",
    "開發金",
    "玉山金",
    "元大金",
    "兆豐金",
    "台新金",
    "新光金",
    "國票金",
    "永豐金",
    "中信金",
    "第一金",
    "王道銀",
    "日盛金",
    "上海銀",
    "合庫金",
    "永豐金",
    "國票金",
    "開發金",
    ]

result_data = dict()
for url in url_list[0:]:
    # url = "http://fund.hncb.com.tw/w/wr/wr04.djhtm?a=ACGC09-003004"
    print(url)

    html = getStockHtml(url)
    dist = parserStockData(html)
    # print(dist)

    for d in dist:

        # if type(d['share']) == int:
        #     stock_share = int(d['share'])
        # elif (type(d['share']) == str) and (d['share']).isdigit():
        #     stock_share = int(d['share'])
        # else:
        #     continue
        stock_share =  convertToNumber(d['share'])

        # 排除債券等其他不是股票標的
        if stock_share == -1:
            continue

        stock_name = d['name']
        if stock_name in result_data:
            share = result_data[stock_name] + stock_share
        else:
            share = stock_share

        result_data[stock_name] = share

# 不排序直接寫入 csv
# print("result_data",result_data)
# with open('output.csv', 'w', newline='') as csvfile:
# #     # 建立 CSV 檔寫入器
#     writer = csv.writer(csvfile)
#     writer.writerow(['股票名稱','股數(千股)'])
#     for name in result_data.keys():
#         # print([name,'{:,}'.format(int(result_data[name]))])
#         writer.writerow([name,int(result_data[name])])

result_list=[]
for name in result_data.keys():
    result_list.append((name,int(result_data[name])))
# print(result_list)
result_list = sorted(result_list, key = lambda s: s[1], reverse = True)
# print(result_list)
with open('output.csv', 'w', newline='') as csvfile:
#     # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerow(['股票名稱','股數(千股)'])
    for result in result_list:
        print(result[0],result[1])
        if result[0] in exclude_stock:
            continue
        writer.writerow([result[0],result[1]])
