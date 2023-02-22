# https://curlconverter.com/
import requests


def main():
    cookies = {
        'rerf': 'AAAAAGP2UHeE+/k8AxMmAg==',
        'ipp_uid': '1677086839499/cXu9dU4lCQrIu7Oj/hWMbotnYnfuq6rmrJ2rRXg==',
        'ipp_key': 'v1677086839499/v33947245ba5adc7a72e273/pF9KdQDZ/aVBFowjZTFwXw==',
        'lang': 'ru',
        'city_path': 'kaluga',
        'current_path': 'd336f80ece5976b84ac120733d85d9c36efdbc223755727136312eae72d77d78a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A114%3A%22%7B%22city%22%3A%22ec54f017-3053-11e1-ae41-001517c526f0%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu043b%5Cu0443%5Cu0433%5Cu0430%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D',
        '_gid': 'GA1.2.307397273.1677086840',
        '_gcl_au': '1.1.259025235.1677086841',
        'tmr_lvid': '8aa903327ab11227082cc93a2f690f74',
        'tmr_lvidTS': '1677086840701',
        '_ym_uid': '1677086841209941246',
        '_ym_d': '1677086841',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'PHPSESSID': '29b31790b618b9305deff4e8cbea2e24',
        '_csrf': 'e0e274d308e7858fe1a900561bcca32c2b70385bd0c29da8db071365dabb3850a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222p_X-_SlOnVFc6M1g4YE_w9OtM9h8L-5%22%3B%7D',
        'rrpvid': '532438448579552',
        'rcuid': '63f3a335e940788e4f4da667',
        'cartUserCookieIdent_v3': '5feface6c5f4dbd5eb56bc9d789cf7c371d0b2b468861a6a4571a52b8ba414a4a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a0081aa2-56a1-3ae4-9f74-8e74125e6241%22%3B%7D',
        'phonesIdent': '686dea5187936d537d69f84d7aeb323eb2b59e16fb144e3b768dd46efcc40d82a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2294e10aab-ba12-448c-8624-bac182392ac1%22%3B%7D',
        '_ab_': '%7B%22mobile-filters-position%22%3A%22current_position%22%7D',
        '_ga_FLS4JETDHW': 'GS1.1.1677086841.1.1.1677086888.13.0.0',
        '_ga': 'GA1.2.1378490326.1677086840',
        'tmr_detect': '0%7C1677086891499',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'rerf=AAAAAGP2UHeE+/k8AxMmAg==; ipp_uid=1677086839499/cXu9dU4lCQrIu7Oj/hWMbotnYnfuq6rmrJ2rRXg==; ipp_key=v1677086839499/v33947245ba5adc7a72e273/pF9KdQDZ/aVBFowjZTFwXw==; lang=ru; city_path=kaluga; current_path=d336f80ece5976b84ac120733d85d9c36efdbc223755727136312eae72d77d78a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A114%3A%22%7B%22city%22%3A%22ec54f017-3053-11e1-ae41-001517c526f0%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0430%5Cu043b%5Cu0443%5Cu0433%5Cu0430%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D; _gid=GA1.2.307397273.1677086840; _gcl_au=1.1.259025235.1677086841; tmr_lvid=8aa903327ab11227082cc93a2f690f74; tmr_lvidTS=1677086840701; _ym_uid=1677086841209941246; _ym_d=1677086841; _ym_isad=2; _ym_visorc=b; PHPSESSID=29b31790b618b9305deff4e8cbea2e24; _csrf=e0e274d308e7858fe1a900561bcca32c2b70385bd0c29da8db071365dabb3850a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222p_X-_SlOnVFc6M1g4YE_w9OtM9h8L-5%22%3B%7D; rrpvid=532438448579552; rcuid=63f3a335e940788e4f4da667; cartUserCookieIdent_v3=5feface6c5f4dbd5eb56bc9d789cf7c371d0b2b468861a6a4571a52b8ba414a4a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22a0081aa2-56a1-3ae4-9f74-8e74125e6241%22%3B%7D; phonesIdent=686dea5187936d537d69f84d7aeb323eb2b59e16fb144e3b768dd46efcc40d82a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%2294e10aab-ba12-448c-8624-bac182392ac1%22%3B%7D; _ab_=%7B%22mobile-filters-position%22%3A%22current_position%22%7D; _ga_FLS4JETDHW=GS1.1.1677086841.1.1.1677086888.13.0.0; _ga=GA1.2.1378490326.1677086840; tmr_detect=0%7C1677086891499',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    response = requests.get(
        'https://www.dns-shop.ru/catalog/3c5037e639df7fd7/posudomoechnye-mashiny/',
        cookies=cookies,
        headers=headers,
    )

    with open("result.html", "w") as file:
        file.write(response.text)


if __name__ == "__main__":
    main()
