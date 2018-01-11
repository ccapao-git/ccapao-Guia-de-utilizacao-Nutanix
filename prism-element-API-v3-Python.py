import nutanix
import urllib3
import ssl
from pprint import pprint

print (ssl.OPENSSL_VERSION)
# Requer suporte TLS v1.2 (e.g.: OpenSSL v1.0.1 ou superior)

urllib3.disable_warnings()

# Configure HTTP basic authorization: basicAuth
nutanix.configuration.host = 'https://prismipaddress:9440/api/nutanix/v3'
nutanix.configuration.username = 'yourusername'
nutanix.configuration.password = 'yourpassword'
nutanix.configuration.verify_ssl = False
nutanix.configuration.debug = False

body = {
        "spec": {
            "resources": {
            },
            "name": "createdbypythonscript"
        },
        "api_version": "3.0",
        "metadata": {
            "kind": "vm",
            }
    }

# create an instance of the API class
api_instance = nutanix.VmsApi()

try:
    # Create a VM
    api_response = api_instance.create_vm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmsApi->create_vm: %s\n" % e)

