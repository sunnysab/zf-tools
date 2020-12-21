class URL:
    # Server address for jwxt
    HOME = 'http://jwxt.sit.edu.cn'

    LOGIN = HOME + '/jwglxt/xtgl/login_slogin.html'
    RSA_PUBLIC_KEY = HOME + '/jwglxt/xtgl/login_getPublicKey.html'


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 ' \
             'Safari/537.36 Edg/87.0.664.66 '
REQUEST_OPTION = {
    'User-Agent': USER_AGENT
}