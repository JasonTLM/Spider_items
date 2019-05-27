# coding=utf-8
import requests

data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}

headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20190511211123-f678c486-2cd9-4594-9b57-febb5cddcf16; _ga=GA1.2.1871190272.1557580284; LGSID=20190511211123-46c048da-73ee-11e9-9f06-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0tbFB0FNkUsj4zIuT00000ZBec7C00000XTqw3n.THd_myIEIfK85yF9pywd0Znqryf4rymLnHRsnj0sujPhP6Kd5HcdnbP7rRF7wWRdPYwawHwjwHwjnW6vwHw7PWujnWcY0ADqI1YhUyPGujY1nWcLnWD4PjD1FMKzUvwGujYkP6K-5y9YIZK1rBtEILILQhk9uvqdQhPEUiq_my4bpy4MQgK9uvRETAnETvN9ThPCQh9YUysOIgwVgLPEIgFWuHdVgvPhgvPsI7qBmy-bINqsmvFY0APzm1Yvn1bkn0%26tpl%3Dtpl_11534_19713_15764%26l%3D1512094584%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3227219413_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D7%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3Dlagou%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGUID=20190511211123-46c04c5b-73ee-11e9-9f06-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557580284,1557580292; JSESSIONID=ABAAABAABEEAAJAF7A16349CAFD3B08F20E587E5104BD34; _gid=GA1.2.1440676095.1557580322; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_search; _gat=1; sm_auth_id=b9f6zmm9rsfexalc; LG_LOGIN_USER_ID=921c9be1e590b565ea6366e695bcd3cfeca74d6f33c454dd92cc2c263137d612; LG_HAS_LOGIN=1; _putrc=22F9E4EFBB68F9FE123F89F2B170EADC; login=true; unick=%E6%9D%8E%E5%9B%BD%E6%B3%89; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=3ac13b32a7d9888d505ed2ed70f242f1e9a122d767048532e8f9ec56a5f77d7e; X_HTTP_TOKEN=570bfe29d3bd1be73091857551b6f7c605949b4f26; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557581903; LGRID=20190511213823-0c360160-73f2-11e9-9f06-5254005c3644; SEARCH_ID=06390b84148244e882a3d02f626b6cca',
    'DNT': '1',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',headers=headers,data=data)

print(response.content.decode('utf-8'))