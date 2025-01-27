import phonenumbers

from mynumber import number

from phonenumbers import geocoder
samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))