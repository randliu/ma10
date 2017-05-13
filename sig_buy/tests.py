from django.test import TestCase

# Create your tests here.
class A:
	def a(self):
		print "a()"
	a="method a"


aa=A()

aa.a()
print aa.a