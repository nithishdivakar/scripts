from tinydb import TinyDB, Query, where
from optparse import OptionParser
from time import gmtime, strftime


NOW = gmtime()
DB = TinyDB("mess.json",indent=2)


def add_new_entry():
    D = strftime("%d", NOW)
    M = strftime("%m", NOW)
    Y = strftime("%y", NOW)
    host = raw_input("Host :")
    day  = raw_input("Day  [{}]:".format(D)) or D
    month= raw_input("Month[{}]:".format(M)) or M
    year = raw_input("Year [{}]:".format(Y)) or Y
    mess = raw_input("Mess [{}]:".format("A")) or "A"
    session = raw_input("Session {B|L|S|D} ?:")
    
    session = session.upper()
    host = host.lower()
    
    assert(session in ["B","L","S","D"])
    assert(host is not None)
    assert(host)
    
    DATA = {
        'host'   : host,
        'day'    : day,
        'month'  : month,
        'year'   : year,
        'session': session,
        'mess'   : mess,
    }
    DB.insert(DATA)
    print "Successfully recorded"


def print_month_usage(): 
    month = raw_input("Month :")
    year  = raw_input("Year  :")
    assert(month)
    assert(year)
    R = DB.search((where('year') == year) & (where('month')==month))
    R.sort(key=lambda x: (x['mess'],x['host'],int(x['day']),["B","L","S","D"].index(x['session'])))
    messes = set([r['mess'] for r in R])
    hosts  = set([r['host'] for r in R])
    days   = set([r['day' ] for r in R]) 
    print ""
    print "Summary for month {}".format(month)
    for mess in messes:
        print "Mess : {}  ".format(mess),
        for host in hosts:
            print "Host : {}".format(host)
            for day in sorted(days, key=lambda x:int(x)):
                print "{:2s} ".format(day),
                D = [r for r in R if r['mess']==mess and r['host']==host and r['day']==day]
                D.sort(key=lambda x: (["B","L","S","D"].index(x['session'])))
                for d in D:
                    print d['session'],
                print ""

parser = OptionParser()
parser.add_option("-n","--new"   ,action="store_true", dest="add_new", help="add new entry")
parser.add_option("-s","--summary"   ,action="store_true", dest="summary", help="summary of a month")

(options, args) = parser.parse_args()

if options.add_new :
    add_new_entry()

if options.summary:
    print_month_usage()
