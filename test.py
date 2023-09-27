wifi_dumps=[{'_type': 'location', 'BSSID': '92:50:ca:b5:f3:70', 'SSID': '1003 Wifi', 'acc': 43, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'w', 'created_at': 1695844235, 'lat': 43.6690838, 'lon': -79.3722382, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844234, 'vac': 4, 'vel': 2},
{'_type': 'location', 'BSSID': '92:50:ca:b5:f3:70', 'SSID': '1003 Wifi', 'acc': 43, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'w', 'created_at': 1695844240, 'lat': 43.6690838, 'lon': -79.3722382, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844234, 'vac': 4, 'vel': 2},
{'_type': 'location', 'BSSID': '92:50:ca:b5:f3:70', 'SSID': '1003 Wifi', 'acc': 54, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'w', 'created_at': 1695844245, 'lat': 43.6689972, 'lon': -79.3722396, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844245, 'vac': 4, 'vel': 6},
{'_type': 'location', 'BSSID': '92:50:ca:b5:f3:70', 'SSID': '1003 Wifi', 'acc': 56, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'w', 'created_at': 1695844250, 'lat': 43.6689926, 'lon': -79.3723008, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844247, 'vac': 4, 'vel': 6}]


m_dumps=[{'_type': 'location', 'acc': 49, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'm', 'created_at': 1695844266, 'lat': 43.6689507, 'lon': -79.3720869, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844266, 'vac': 4, 'vel': 4},
{'_type': 'location', 'acc': 128, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'm', 'created_at': 1695844293, 'lat': 43.6684459, 'lon': -79.37237, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844293, 'vac': 4, 'vel': 9},
{'_type': 'location', 'acc': 44, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'm', 'created_at': 1695844310, 'lat': 43.6684002, 'lon': -79.3724782, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844310, 'vac': 4, 'vel': 0},
{'_type': 'location', 'acc': 229, 'alt': 100, 'batt': 53, 'bs': 1, 'conn': 'm', 'created_at': 1695844326, 'lat': 43.6689683, 'lon': -79.3720356, 'm': 2, 'tid': '1', 'topic': 'owntracks/praveen/1', 'tst': 1695844325, 'vac': 4, 'vel': 1}
]

x=list(wifi_dumps[0].keys())
m=list(m_dumps[0].keys())

print(sorted(x)[2:])
print(sorted(m))

# import datetime
# t=[1695845602824000000,1695845607906000000,1695845612924000000,1695845618132000000,1695845622963000000]
# for i in t:
#     x=i/1e9
#     print(datetime.datetime.fromtimestamp(x))