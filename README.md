# cashify-python-etcd

Cashify Python Repo to get Key values from ETCD.

Pre-requisite:
1. python-etcd library


How to use:
- Import cashifypythonetcd and init class with parameters "host, protocol, port, app_name"
- Use function "get_property_value" with parameters "key, service_version, default" with class instance to get value from ETCD
_ If key is not defined in ETCD, we will get the default value back
