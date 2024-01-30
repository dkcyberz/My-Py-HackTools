import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def filter_valid_ips_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        ip_list = file.read().splitlines()

    valid_ips = [ip if ':' not in ip else f'[{ip}]' for ip in ip_list if validate_ip(ip)]

    with open(output_file, 'w') as valid_ip_file:
        valid_ip_file.write('\n'.join(valid_ips))

# Example usage:
input_file_path = input("Input_File_Path : ")
output_file_path = 'validip.lst'

filter_valid_ips_from_file(input_file_path, output_file_path)
print("Valid IP addresses stored in", output_file_path)
