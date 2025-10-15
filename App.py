import requests
import json


# Card Details (easily editable)
cc = '5598880399472598' # Card Number (Note: This is likely a test card number)
cvv = '857'            # CVC/CVV
mm = '01'              # Expiration Month (MM)
yy = '26'              # Expiration Year (YY)
#first request


headers = {
    'accept': 'application/json',
    'accept-language': 'hi-IN,hi;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10001&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Ffae42e56c7%3B+stripe-js-v3%2Ffae42e56c7%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Forevaa.com&time_on_page=59434&client_attribution_metadata[client_session_id]=25ac57eb-34d5-4d25-a0d8-59b486e7c282&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=e497e03d-3191-4699-8db1-63877470654f&guid=10a5a6c7-bd3e-4730-96b8-777bb4fb4abde8e848&muid=06785c71-1d7a-4590-b3ed-47183a0854e4f3eb45&sid=7429db73-82f1-48b9-a6c5-6aba5028917df22868&key=pk_live_51BNw73H4BTbwSDwzFi2lqrLHFGR4NinUOc10n7csSG6wMZttO9YZCYmGRwqeHY8U27wJi1ucOx7uWWb3Juswn69l00HjGsBwaO&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzYwNDY1MTc1LCJjZGF0YSI6IkdKS3h1QmovU2RBS3o3YkVlVDc5U3V4YkU0VU1rSHFNaG04eFYrUWNrMitiUk5yM2MwbkM3M1MzbUdYQWJkSjJUYStiY1phME9nL1NDSVhZdUN6aUx2TjJDeENkVGlSQmpsck5BeUJrVVU1eUtaN0VDcXd2RkZvaGk2cGhleW1KMTVIa1dKSWU0T1dHS1AyZEtBaUpLM0xVL0pRY0M4K1dTOXdkTXc2ZTBsNTc5OXcxNDlZbE1BakNBYjR4RzdVZXNhS3RyWHh6N0hld21BZXUiLCJwYXNza2V5IjoidnRMR3dZV1IvQXBPNnpIRzlHc1BRUGNYRFZzem9DZTRGVGJxY1gwaTZnM0xhQVpuQy9zcWtDa00zN0k0cWY3NnJoTTFyOEZLNDFoRXhzbGZVMzFCazMycURGLzlwa2ZaUW9MRlZlS2FUTmRDTmNTcm56Um9jY0RmUDh4Y3Z6cDhmS0ZIY096end0dHVoSTJuWjFKN1o4SDBINS9FWm5odWg0UnZqbEMrWXVScUtlV2ZidlhLY0s0NUtPK1lQTnVENlh1dmRocTI5TmNYM2svWXBtRlUxbFMrOUZoRkNxSWswU05TWDkzSGpwUmNxUzduRkJhSWNiTHdJWlFqUnpjd0RkRGh0Y1dyeHRpOGpWaXBCZGZhbjREc2FPUUV1Tkl2S3BWaVQ1eStTOXkyVG9yTERNSENrSENESXFGM3pJb3RJMHI0aTRqczQya3ZuWHI3ZWVIZHI2dmdRK1h6QUFhc2NVYTl0WllOSUc3eWpRVGVtYlhueW8xQWowQmpTQklnTVA1V0VpaUxNM1M2QUxpRXY2T2lDUE5xUFhaWXorM21rRVo0UnhYUXVRWkw2b0IvK3VHUklqbjhSR09pTTJNaVRIL00xMVJpemMyNEp6emVybldrM0RyaHJxOU5QaXZvVHhzYmV2MXJvL2xJamg5UGpJeXlUY1VsVzh5L2E1N0J1aERJUW13NEJGa0t6b00wSGJwc2Q0ZlNwbTVmUWo3YWFJbmw3S1dkT2tteTh5MDBocHd0T0lSRFNPWCsrSmM2Qi83Q1o1SG1IRTdTMW1qYTVhUWtBejk5MXJyamgySkJadVc1MHBsQ0ZuZENJOE5seWhIaWt6dlB4QzJCZVdVWEZFSXRHMXhCV0d6OHNlZld2QjVoZ3k5bmtRK1FpSHltd3MxSjJ2Tld6WldZUFhQd09ISFdQZzA1RUwzTFNhdU5DZGFiejh5YzB1RUE3M2tvc3lUdFFjWEJrdDVvVkkzMWRNQzhkeDBHdHppMGlsRW9zbjEwSldYN2ZEbHRFLzdPdVQwc2VSb080L1BhcmFkSmVQMWF2U0RyOEx4NWRwWGJGM21aZ2VaRERjd1IxS2o0V0RsaFBPNkE1MWJnTElJWEJPMVBRcU9MejZDUDZCRTlySnRSVTFnQ0JjZFZISlZxUGg4NEVzakJQc0RrOXNpSi81RExmTDVHc2VIMWpyV2xDMkR4ZTBSOW1tZHhjNTFJY2xmT0JEeDAvUm9POWMzeFpkSFpjclFJU2RabjBDSnFMRlNrQW1nL1VhcEJKUXNCM0NyRE1qMGVBdkh3T3E5ak9tSEpMcVNad3NaeXV6N1dGN3pzU3BNbk5XdjFudW5iRDlhRHN3WmljQytuMlo1UUp3UDhRQ2ZyTTZlQ0s5aUliSWNDenJjcW1oMmRoRVFJWFR2MkdpTG5sWERHRUxGZllmRUwrbTFDZndwdzVBUExOYUFrSlljY2JBbjdkUEFVeHNUSjMwTGgzWGlxenloVWxWb2taY2pWUEM4YXNvQXhWTHBuVDB3eWNvanlxazl4dGxwN3hFSVVKbDFlZkZKMTBDVEhyejAvNDFEa2tzQnhBY1YxVkNVNUduUVhiZ2NPVm5ZNExuUUVualVsb2JnV0R0Q1dmY21yUXdCZTVReXBmRnZMVzluMzgveWRQQjZuS2QrRTl1TTVjK1pJcjhscTVLZHVOam4wWnlvUzJUakI2c0J1U1dNZ1k3amc1dGl1QnByZjcrVUJoSUpkWkZEbGxkTGcybEVXeUtiemt1R0laZkh5bVdXN3NuK3JJR05ZZzdkQ3lMQTllU3pkbEJwbFlnV1llQ0plWjNCS2xGbFgwQWpzNldKb2ZyRUlsYzhScjVCNCs3TUQ5TnpFajhKdHFlT0t5dWtaT213NE9RNHZDWjBFM0xSaWR6blFqVE55NnRqUmRVWVBDdXMwc3JmcFF4czhvRHVUOEgxd3hmbHFOckNpb0pSckdPZFl5RkFZTkRYcCtGekVUZjlLUlpoeU8xM2FLcHBNWXlHM1MrVzR3MStSUlE5UkdJUDRuNjh2RCs4VTEwRElCS00wSWJiQ2EwUVJCUnR5eDFvWnNvSlVWQUUyRWlDV1l4SWdsUkYxbC9seWJMblN3RGVGeHRRclZQWWI1dkhaUmVGRlVXTzdxNHI2MWtoOStTNEtUUjVMbTZMVFlVMnF5RXVUbEV6bURaazJZL3hXSEVlYTNqWWZFOXVlZmxPSjBQNWd6S2RUc0tmRmEzRStLb3oxYVJRT3IwdnlZbEFEU0pqZXBUWU9hQjJrUENkVmJhczVoRGdKVng5ZHcwNEEzNnBpaURxWUZqTkw3dHpFaW5zMGdGdXBTVXQybWwzdGJheFVNaklrd2ZVSXZuR2NweUQwOWcwZkp2b3Q3ZGxtQkN6b0RnZE1VTE44V1FTek45bE0iLCJrciI6IjJjZmNkMjNhIiwic2hhcmRfaWQiOjI1OTE4OTM1OX0.MAZweSeLNYdAVUiqVx_lc1tSewWTCftzBFxmmRFMQnM'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

pm_id = response.json()

id = pm_id['id']



# second request

cookies = {
    'wordpress_sec_13d597ccaacdb3aa9062bb289246a418': 'pehevop285%7C1761674647%7CN7HGy6OI9Faxw6vNfW1t7pyRBhDFXtRFj7nRTBsxG7F%7Cf99341216e4597115713e15c426ecbe5cfc2a40739ec9e5eacaf3570c5c59081',
    'current_cur': 'USD',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-10-14%2017%3A34%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-10-14%2017%3A34%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F141.0.0.0%20Safari%2F537.36',
    '_ga': 'GA1.1.1779341087.1760465043',
    '__stripe_mid': '06785c71-1d7a-4590-b3ed-47183a0854e4f3eb45',
    '__stripe_sid': '7429db73-82f1-48b9-a6c5-6aba5028917df22868',
    'mailchimp.cart.current_email': 'pehevop285@cerisun.com',
    'MCPopupClosed': 'yes',
    '_gcl_au': '1.1.1624443767.1760465043.488256518.1760465045.1760465047',
    'mailchimp_user_email': 'pehevop285%40cerisun.com',
    'wordpress_logged_in_13d597ccaacdb3aa9062bb289246a418': 'pehevop285%7C1761674647%7CN7HGy6OI9Faxw6vNfW1t7pyRBhDFXtRFj7nRTBsxG7F%7Cbd118032b29e437618c3907e9607a4e0c56b69b35339b29bbd15c5c02ce0c915',
    '_ga_K69YGD2930': 'GS2.1.s1760465043$o1$g0$t1760465049$j54$l0$h0',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F',
}

headers = {
    'accept': '*/*',
    'accept-language': 'hi-IN,hi;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://orevaa.com',
    'priority': 'u=1, i',
    'referer': 'https://orevaa.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'wordpress_sec_13d597ccaacdb3aa9062bb289246a418=pehevop285%7C1761674647%7CN7HGy6OI9Faxw6vNfW1t7pyRBhDFXtRFj7nRTBsxG7F%7Cf99341216e4597115713e15c426ecbe5cfc2a40739ec9e5eacaf3570c5c59081; current_cur=USD; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-10-14%2017%3A34%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-10-14%2017%3A34%3A03%7C%7C%7Cep%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F141.0.0.0%20Safari%2F537.36; _ga=GA1.1.1779341087.1760465043; __stripe_mid=06785c71-1d7a-4590-b3ed-47183a0854e4f3eb45; __stripe_sid=7429db73-82f1-48b9-a6c5-6aba5028917df22868; mailchimp.cart.current_email=pehevop285@cerisun.com; MCPopupClosed=yes; _gcl_au=1.1.1624443767.1760465043.488256518.1760465045.1760465047; mailchimp_user_email=pehevop285%40cerisun.com; wordpress_logged_in_13d597ccaacdb3aa9062bb289246a418=pehevop285%7C1761674647%7CN7HGy6OI9Faxw6vNfW1t7pyRBhDFXtRFj7nRTBsxG7F%7Cbd118032b29e437618c3907e9607a4e0c56b69b35339b29bbd15c5c02ce0c915; _ga_K69YGD2930=GS2.1.s1760465043$o1$g0$t1760465049$j54$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Forevaa.com%2Fmy-account%2Fadd-payment-method%2F',
}

data = {
    'action': 'wc_stripe_create_and_confirm_setup_intent',
    'wc-stripe-payment-method': id,
    'wc-stripe-payment-type': 'card',
    '_ajax_nonce': 'aef92d4a86',
}

response = requests.post('https://orevaa.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

print(response.text)
