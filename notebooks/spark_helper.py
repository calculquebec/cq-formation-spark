import pyspark
import re

def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    m = regex.match(path)
    d = m.groupdict() if m is not None else None

    return d

def get_app_dashboard_url(sc):
    if not isinstance(sc, pyspark.SparkContext) or len(sc.master) == 0:
        raise Exception("get_dashboard_url requires a valid SparkContext as argument.")
    
    if sc.master == 'local[*]':
        url = "http://localhost:4040"
    else:
        hostname = url_path_to_dict(sc.master)['host']
        url = "http://{hostname}:4040".format(hostname=hostname)
    return url