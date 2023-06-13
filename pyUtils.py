
#
#  Get Options
#
def parseOpts():
    from optparse import OptionParser
    p = OptionParser()
    p.add_option('--output',   type = 'string', default = "plots",          dest = 'output',     help = 'output dir' )
    (o,a) = p.parse_args()

    
    return (o,a)
