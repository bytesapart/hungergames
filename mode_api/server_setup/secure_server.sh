hosts="13.232.190.195 65.1.135.89 15.206.169.114 13.233.237.248 3.108.61.77 3.108.42.239 15.206.145.158 52.66.204.246 13.233.113.252 13.127.218.137 65.2.9.243 13.233.167.94 15.206.117.200 13.126.226.62 15.206.125.233 13.126.33.199 3.6.92.15 3.6.38.116 13.235.246.134 13.233.132.11" 
for host in $hosts 
do 
	ssh-keyscan -H $host >> ~/.ssh/known_hosts
	scp squid.conf "ubuntu@${host}:/home/ubuntu" 
	ssh -t "ubuntu@${host}" sudo -p sbc_adm cp /home/ubuntu/squid.conf /etc/squid/squid.conf
	ssh -t "ubuntu@${host}" sudo -p sbc_adm service squid restart
done
