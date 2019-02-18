import uuid


fqdn = "beacon.tokyo-ondai.ac.jp"
uid = uuid.uuid5(uuid.NAMESPACE_DNS, fqdn)

print(uid)
