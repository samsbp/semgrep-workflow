import requests,os

authToken = "Token "+os.getenv('AUTH_TOKEN')
url = 'http://34.29.23.123/api/v2/import-scan/'
headers = {'Authorization': authToken}
files={'file': open("semgrep.sarif","rb"),'active':(None,'true'),'skip_duplicates':(None,'true'),'deduplication_on_engagement':(None,'true'),'verified':(None,'true'),'close_old_findings':(None,'true'),'engagement_name':(None,'Github Semgrep'),'minimum_severity':(None,'Info'),'close_old_findings_product_scope':(None,'false'),'create_finding_groups_for_all_findings':(None,'true'),'product_name':(None,'Semgrep Project 2'),'scan_type':(None,'SARIF')}
r = requests.post(url, headers=headers,files=files ,verify=True) # set verify to False if ssl cert is self-signed

print(r.status_code,r.text)
