import io
import pycurl
from time import gmtime, strftime
import stem.process
from stem.util import term
# reference: https://stem.torproject.org/tutorials/to_russia_with_love.html

SOCKS_PORT = 7000

# generated by 1.3.2_find_exitnodes.py
countries_with_exit_node = ['us', 'de', 'ch', 'ru', 'no', 'at', 'se', 'nl', 'bg', 'fr', 'be', 'sg', 'ua', 'vn', 'lu', 'mx', 'lt', 'vg', 'jp', 'es', 'ca', 'sk', 'ee', 'hu', 'am', 'lv', 'gr', 'tw', 'fi', 'gb', 'kw', 'is', 'ro', 'cz', 'tr', 'hk', 'md', 'ar', 'pl', 'gt', 'in', 'sa', 'id', 'br', 'au', 'pa', 'nz', 'si', 'dk', 'za', 'pt', 'hr', 'it', 'kz', 'lr', 'ie', 'eg', 'kr']

url = "http://dogo.ece.cmu.edu/tor-homework/secret/"

def query(country):
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
    # get http code, should be either 403 or 200
    code = query.getinfo(pycurl.HTTP_CODE)
    # get current time
    t = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    if (code == 200):
      # output country name and time once get 200 response code
      print "Country:%s verified at %s" % (country, t)
    return
  # query failed with exception
  except pycurl.error as exc:
    return

# print bootstrap info
def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    return

# traverse all countries with exit node
for country in countries_with_exit_node:
  try:
    # Start tor instance with given exit node country
    tor_process = stem.process.launch_tor_with_config(
      config = {
        'SocksPort': str(SOCKS_PORT),
        'ExitNodes': ('{' + country + '}'),
      },
      init_msg_handler = print_bootstrap_lines,
    )
    # run query
    query(country)

    # Stop tor instance
    tor_process.kill()
  except:
    continue
