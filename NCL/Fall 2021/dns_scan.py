import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['resolver.liber8tion.cityinthe.cloud']
resolver.port = 1055

for line in open('hosts.txt'):
    try:
        result = resolver.resolve(line, 'A')
        for ipval in result:
            print(f'{line} {ipval.to_text()}')
    except dns.resolver.NoAnswer:
        print(f'{line} TryAgain')
