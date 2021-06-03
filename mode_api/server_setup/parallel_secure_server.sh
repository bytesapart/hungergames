parallel-scp -h pssh_hosts_files squid.conf /home/ubuntu/squid.conf
parallel-ssh -i -h pssh_hosts_files sudo -p sbc_adm cp /home/ubuntu/squid.conf /etc/squid/squid.conf
parallel-ssh -i -h pssh_hosts_files sudo -p sbc_adm service squid restart
