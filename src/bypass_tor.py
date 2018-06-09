import io
import pycurl
import time
# reference: https://stem.torproject.org/tutorials/to_russia_with_love.html

SOCKS_PORT = 7000

url = "https://duckduckgo.com/"

def query():
  output = io.BytesIO()
  # connect to webserver with pycurl
  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    # return the query output from webserver
    return output.getvalue()
  # query failed with exception
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)

# Time the query without tor
print "1. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "2. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "3. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "4. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "5. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "6. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "7. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "8. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "9. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

print "10. Connecting to %s without tor..." % url
start_time = time.time()
query()
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)
