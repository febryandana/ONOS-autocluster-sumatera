# ONOS_autocluster
This script is intended to automatically deploy an ONOS cluster, original work by [ederollora/ONOS_autocluster](https://github.com/ederollora/ONOS_autocluster)  
Also thanks to [abazh/ONOS_autocluster](https://github.com/abazh/ONOS_autocluster/)  
<img src="sumatera_topology.png" width="640">


## Prerequisite (you may skip it if already installed)
- Docker engine installed on your Ubuntu server with a non-user privileges to access all docker commands, use this [link](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
- [Mininet](http://mininet.org/download/#option-3-installation./-from-packages)
- `$ sudo apt install jq python-is-python2`

## Steps to do
1. Run `$ git clone https://github.com/febryandana/ONOS-autocluster-sumatera.git`
> You may encounter problem when running the script if jq and python2 is not install on your server
> Just install the dependencies `$ sudo apt install jq python-is-python2`
2. Go the directory `$ cd ONOS-autocluster-sumatera`
3. Create ONOS cluster (by default 2 instances) `$ ./create_cluster.sh`
4. Set sshkey and env parameters `$ ./set_env_sshkey.sh`
5. Check environment variables using `$ env` make sure there is ONOS variables (ONOS_INSTANCES, OCI, OC1, OC2, ONOS_ROOT, ONOS_BIN, and PATH to ~/onos/bin)
> If you cant find them, execute `$ ./onos_env.sh` to reload the source file.  

## Testing using sumatera-map.py
You can use [Tmux](https://github.com/tmux/tmux/wiki) to easily switch between program without closing the program. It's useful when used with mininet so that the topology wont disconnect  
> sumatera-map.py consists of 8 switches and 13 hosts
- Go to directory `$ cd ONOS_autocluster`
- Run the onos-netfcg `$ onos-netcfg $OC1 sumatera-map.json`
> setting the label name of the switches and hosts in ONOS
- Run the example `$ sudo python3 sumatera-map.py $ONOS_INSTANCES`
- In the mininet shell `> pingall` or `> h1 ping h5`
> Run the topology and connected all switches to the two ONOS Instances  
> It should resulted as error or 100% dropped because we did not activate forwarding apps yet
- On the other terminal, run `onos`
> it will direct you to ONOS CLI, you can just press TAB to see other command completion
- You may activate the necessary ONOS app, `$ app activate fwd` or 
- checking paths between two switches `$ paths --disjoint of:0000000000000001 of:0000000000000003`
- use CTRL+D or `$ logout` to disconnect from ONOS CLI
- Go to ONOS GUI with your web browser to open http://[your_ip_address or localhost]:8181/onos/ui
