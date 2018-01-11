{
  "metadata": {
    "kind": "webhook"
  },
  "spec": {
    "name": "vm_notifications_webhook_01",
    "resources": {
      "post_url": "http://ipaddress/incoming.html?test=successful",
      "events_filter_list": [
        "VM.ON",
        "VM.OFF"
      ]
    },
    "description": "Notifications for VM events."
  },
  "api_version": "3.0"
}
