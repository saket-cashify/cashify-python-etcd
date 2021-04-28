# cashify-python-etcd

Cashify Python Repo to get Key values from ETCD.

Pre-requisite:
1. python-etcd library (https://pypi.org/project/python-etcd/)


How to use:
1. Use steps under if want to use directly from source code
- Install library using pip install git+https://git@github.com/saket-cashify/cashify-python-etcd.git
- Import cashifypythonetcd and init class with parameters "host, protocol, port, app_name"
- Use function "get_property_value" with parameters "key, default" with class instance to get value from ETCD
- If key is not defined in ETCD, we will get the default value back
- add this line to requirements file to install "-e git+https://git@github.com/saket-cashify/cashify-python-etcd.git#egg=cashifypythonetcd" automatically

2. Use these steps to use from PyPi
- pip install cashifypythonetcd
- Import cashifypythonetcd and init class with parameters "host, protocol, port, app_name"
- Use function "get_property_value" with parameters "key, service_version, default" with class instance to get value from ETCD
- If key is not defined in ETCD, we will get the default value back
- add cashifypythonetcd==0.0.1 to requirements
