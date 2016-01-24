import pyspark
import re
import hashlib
import os
import tarfile

from urllib.request import urlretrieve
from urllib.parse import urljoin, urlparse

EXT = ('.tgz', '.tar.gz')

CWD =  os.getcwd()

def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def download_check_extract(path, url, files, md5s):
    os.chdir(CWD)    
    # Create destination folder if it does not exist
    if not os.path.exists(path):
        os.makedirs(path)

    # Download archives and verify checkums
    for file_, md5_ in zip(files, md5s):
        file_path = os.path.join(path, file_)
        if not os.path.exists(file_path):
            urlretrieve(urljoin(url,file_), file_path)
        else:
            print('File already downloaded, checking MD5.')
        correct = md5_ == md5(file_path)
        print("{file} {status}".format(file=file_, status=('OK' if correct else 'BAD')))
        
        # Extract tarball if checksum is correct
        if correct:
            if any(file_.endswith(ext) for ext in EXT):
                with tarfile.open(file_path, 'r:gz') as tar:
                    os.chdir(path)
                    tar.extractall()

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
