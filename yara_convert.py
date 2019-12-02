import yara
import json

def compileandsave():
    rules = yara.compile(filepath='./myrule.yara')
    rules.save('./myrule')

  
def loadrule():
    rules = yara.load('./myrule')
    matches = rules.match('./targetfile.py',callback=mycallback)

        
def mycallback(data):
    print(data)
    yara.CALLBACK_CONTINUE


def get_api():

    # api json endpoint 불러옴
    json_data = "./data.json"
    data = json.loads(open(json_data).read())
    # 라인당 하나씩 불러옴 [][] 안에 숫자를 변경하면 값이 변함
    for index in range(0, 2):
        title = data[index]['title']
        endpoint = data[index]['endpoint']
        strapi = "{90,100}"
        rule_data = "rule " + "korea_public_api"+str(index) +"\n{{\n\tmeta:\n\t\tdescription = \"{0}\"\n\tstrings:\n\t\t$apikey0 = /\"{1}\"/\n\t\t$apikey1 = /[0-9A-Za-z%]{2}/\n\n\tcondition:\n\t\t$apikey0 and $apikey1\n}}\n"
        
        # yara rule 에 맞게 변환 & 저장
        f = open('myrule.yara', 'a', encoding='utf-8') 
        f.write(rule_data.format(str(title),endpoint.translate({ ord('/'): '\/' ,ord('?'): '\?'}),str(strapi) ))
'''       
    f = open('myrule.yara', 'r', encoding='utf-8') 
    data1 = f.read()
    print(data1)
'''
if __name__=="__main__":
    get_api()
    compileandsave()
    loadrule()
