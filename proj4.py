import subprocess
port = input("Enter the port to capture packets on: \n")
packets= input("Enter the number of packets to capture: \n")
protocol = input("Enter the protocol (e.g., 'tcp' or 'udp'): \n")
networkint= "lo"

command = f"sudo tcpdump {protocol} -i {networkint} port {port} -c {packets}" 

result = subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output= subprocess.getoutput(command)
if result == 0:
    # Count the number of SSH packets in the captured trace
    ssh_packets = output.count("ssh")
    print(f"Number of incoming SSH packets: {ssh_packets}")
else:
    print(f"An error occurred")