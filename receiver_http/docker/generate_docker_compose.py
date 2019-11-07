docker_compose = 'docker-compose.yaml.template'
service_container = 'service_container.template'
service_ips = 'service_ips.template'

def load_template(template_name):
    fp = open(template_name)
    template = fp.read()
    fp.close()

    return template


while(True):
    try:
        quantity = input('Quantidade de containeres: ')
        quantity = abs(int(quantity))
        break
    except:
        print('Quantity of container must be an integer')

docker_compose_template = load_template(docker_compose)
service_container_template = load_template(service_container)
service_ips_template = load_template(service_ips)

service_ips_result = ''
service_container_result = ''
for i in range(quantity):
    service_container_result += service_container_template.format(index=i)
    service_ips_result += service_ips_template.format(index=i)


#print(service_container_result)
#print(service_ips_result)

dc = docker_compose_template.format(service_container=service_container_result, service_ips=service_ips_result)
fp = open('docker-compose.yaml', 'w')
fp.write(dc)
fp.close()
