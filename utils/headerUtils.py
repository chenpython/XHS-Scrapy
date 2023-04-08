from urllib.parse import urlparse

import utils.XsXtUtils as XsXt


def getHeader(url, param, data, cookie):
    header = {
        'authority': 'edith.xiaohongshu.com',
        'origin': 'https://www.xiaohongshu.com',
        'referer': 'https://www.xiaohongshu.com/',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }
    header.update(XsXt.trace())
    real_url = urlparse(url).path
    if len(param) != 0:
        real_url += '?'
        i = 0
        for k, v in param.items():
            real_url += f'{k}={v}'
            if i != len(param) - 1:
                real_url += '&'
            i += 1
    header.update(
        XsXt.sign(real_url, data))
    header.update(XsXt.XCommonId(cookie['a1'], header['x-t'], header['x-s']))
    header['x-t'] = str(header.get('x-t'))
    return header
