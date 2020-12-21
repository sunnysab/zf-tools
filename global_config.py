class URL:
    # Server address for jwxt
    HOME = 'http://jwxt.sit.edu.cn'

    # Login related
    LOGIN = HOME + '/jwglxt/xtgl/login_slogin.html'
    RSA_PUBLIC_KEY = HOME + '/jwglxt/xtgl/login_getPublicKey.html'

    # Function related
    SCORE_LIST = HOME + '/jwglxt/cjcx/cjcx_cxDgXscj.htm'

# End of class URL


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 ' \
             'Safari/537.36 Edg/87.0.664.66 '
REQUEST_OPTION = {
    'User-Agent': USER_AGENT
}

'''
    Data dictionary.
'''
GLOBAL_DICT = {
    # 学年名
    'academic_year': 'xnm',
    # 学期名
    'semester': 'xqm',
    # 时间戳（年代）
    'timestamp': 'nd',
    # 功能模块代码
    'function_code': 'gnmkdm'
}