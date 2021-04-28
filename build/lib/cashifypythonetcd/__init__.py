import etcd

# Can also use python cache if we want to use it as generic
# Currently using this for Django as use case
from django.core.cache import cache


class CashifyETCD(object):

	"""
	Base class for initalizing
	"""

	etcd_client = None
	app_name = None

	def __init__(self, host, protocol, port, app_name):

		""" Get ETCD client"""

		self.etcd_client = etcd.Client(host=host, protocol=protocol, port=port)
		self.app_name = app_name

	def get_property_value(self, key, default):
		"""
		Get property value from ETCD if not found return default
		"""
		try:
			required_key = self.app_name + '/' + self.app_name + '.' + key
			value = self.get_value_cache(required_key)
			if not value:
				value = self.etcd_client.read(required_key).value
				self.set_value_cache(required_key, value)
			return value
		except Exception as e:
			return default

	def get_value_cache(self, key):
		"""
		Get value from cache
		"""
		return cache.get(key)

	def set_value_cache(self, key, value):
		"""
		Set value in cache for 5 minutes
		"""
		cache.set(key, value, 300)
