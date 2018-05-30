import json
import requests
import urllib3

from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

myMainURL = 'https://prismipaddress:9440/PrismGateway/services/rest/v2.0/'
myUser = 'yourusername'
myPass = 'yourpassword'


class ManageAPI():
    def __init__(self):
        self.mySession = requests.Session()
        self.mySession.auth = HTTPBasicAuth(myUser, myPass)
        self.mySession.verify = False
        self.mySession.headers = {'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json'}

    def get_vms(self):
        toreturn = self.mySession.get(myMainURL + 'vms/')
        return (toreturn)
        # exemplo: myAPI.get_vms()

    def post_vm_clone(self, clonename, vmuuid):
        mypayload = {"spec_list": [{"name": clonename}]}
        mydata = json.dumps(mypayload)
        toreturn = self.mySession.post(myMainURL + 'vms/' + vmuuid + '/clone', data=mydata)
        return (toreturn)
        # exemplo: myAPI.post_vm_clone('vmname','8e9c5956-c015-40fe-b235-c6dc76716099')

    def session_close(self):
        return(self.mySession.close())

myAPI = ManageAPI()
vms = myAPI.get_vms().json()

for vm in vms['entities']:
    vmclone = myAPI.post_vm_clone(vm['name']+'.clone', vm['uuid'])
    # ciclo for vai criar clones das VMs do cluster tendo como resultado o seguinte nome: vmname.clone

myAPI.session_close()
