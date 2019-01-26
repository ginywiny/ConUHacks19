import urllib
import time
import re

offset = '1'
base_url = 'https://conuhacks-playback-api.touchtunes.com/plays?'

get_data = False

if get_data:
    with open('plays_data.json', 'w') as fd:
        fd.write('{"plays":[')

        for month in range(1, 13):
            for day in range(1, 28):

                start_date = '2018-' + str(month).zfill(2) + '-' + str(day).zfill(2) + 'T' + '12:00:00Z'
                end_date = '2018-' + str(month).zfill(2) + '-' + str(day + 1).zfill(2) + 'T' + '23:00:00Z'
                url= base_url + 'startDate=' + start_date + '&endDate=' + end_date + '&offset=' + offset

                headers = {}
                headers['client-secret'] = '9923ac9b-8fd3-421f-b0e5-952f807c6885'

                request = urllib.request.Request(url, headers=headers)            
                response = urllib.request.urlopen(request)

                replaced = re.sub('{"plays":\[', '', response.read().decode('utf-8'))
                replaced = re.sub('\]}', '', replaced) + ','

                fd.write(replaced)

        fd.write(']}')