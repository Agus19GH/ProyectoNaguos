from ast import Import
from urllib import request

import requests
from requests.structures import CaseInsensitiveDict

url = "https://---------/portal/CSPublicQueryService/CSPublicQueryService.svc/json/EncryptQS?user_name=guardiamedica&password=Roentgen1243"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer wyBRLs8EptCOElxG1bOB570q40o%2bYOHkOrFbjjdvF8CqIq6SmHMiIxFRTKqmWlbP"
headers["Content-Type"] = "application/json"

data = '"user_name=------------&password=------------&accession_number=""&patient_id=""'

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print ("https://------------------?urltoken=" == resp.json())

