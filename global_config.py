"""
    Url that probably used in the program.
"""
class URL:
    # Server address for jwxt
    HOME = 'http://jwxt.sit.edu.cn'

    # Login related
    LOGIN = HOME + '/jwglxt/xtgl/login_slogin.html'
    RSA_PUBLIC_KEY = HOME + '/jwglxt/xtgl/login_getPublicKey.html'
    # Page for login success.
    INIT_MENU = HOME + '/jwglxt/xtgl/index_initMenu.html'

    # Function related
    SCORE_LIST = HOME + '/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'
    TIME_TABLE = HOME + '/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N253508'
    PROFILE = HOME + '/jwglxt/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default'
# End of class URL


'''
    Configuration for the spider.
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 ' \
             'Safari/537.36 Edg/87.0.664.66 '
REQUEST_OPTION = {
    'User-Agent': USER_AGENT
}
