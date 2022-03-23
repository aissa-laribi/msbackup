import argparse

known_drivers = ['local', 's3']

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local' & 's3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser=argparse.ArgumentParser(description="""
    Back up MySQL Databases locally or to AWS S3
    """)
    parser.add_argument("user", help="username")
    parser.add_argument("host", help="MySQL Server IP address")
    parser.add_argument("dbname", help="database name")
    parser.add_argument("--driver",
            help="how & where to store backup",
            nargs=2,
            action=DriverAction,
            required = True)
    return parser

def main():
    import time
    import boto3
    import msbackup
    from msbackup import msdump, storage
    import io

    args = create_parser().parse_args()
    dump = msdump.dump(args.user, args.host, args.dbname)
    if args.driver == 's3':
        client = boto3.client('s3')
        print("Backing database up to %s in S3 as %s" % (args.destination, 'msbackup.sql'))
        storage.s3(client, io.BytesIO(dump.stdout), args.destination, 'msbackup.sql')
    else:
         outfile = open(args.destination, 'w+b')
         print(f"Backing database up locally to {outfile.name}")
         storage.local(dump.stdout, outfile)

