=======
Day 03
=======


Decommission your nodes
========================

1. Do the following:

::

	[root@Master ~]# docker node ls
	ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
	sz3d2x0v5optt8wiunz790vkt *   Master     Ready     Active         Leader           20.10.17
	uqf4hswbcrhzu40862iy4elvx     worker1    Ready     Active                          20.10.17
	3xjdz8tenj345y7fc7g73zv79     worker2    Ready     Active                          20.10.17

	[root@Master ~]# docker service ls
	ID             NAME      MODE         REPLICAS   IMAGE          PORTS
	miwzztp61ydw   web       replicated   15/15      nginx:latest   *:8000->80/tcp

	[root@Master ~]# docker stack ls
	NAME      SERVICES   ORCHESTRATOR
	vstack    6          swarm
	wstack    2          swarm

2. Decommission backwards.

stack::

	[root@Master ~]# docker stack rm vstack wstack

Service::

	[root@Master ~]# docker service rm web
	web


Nodes, after doing `docker swarm leave` on worker nodes, the swarm status would become::

	[root@Master ~]# docker node ls
	ID                            HOSTNAME   STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
	sz3d2x0v5optt8wiunz790vkt *   Master     Ready     Active         Leader           20.10.17
	uqf4hswbcrhzu40862iy4elvx     worker1    Down      Active                          20.10.17
	3xjdz8tenj345y7fc7g73zv79     worker2    Down      Active                          20.10.17

The workers are down now, now remove them from swarm cluster::

	[root@Master ~]# docker node rm worker1
	worker1
	[root@Master ~]# docker node rm worker2
	worker2

Finally remove master node from cluster::

	[root@Master ~]# docker swarm leave --force
	Node left the swarm.

We are all set for kubernetes.

Kubernetes
===========

- First orchestrator came in the market.
- Swarm came from Kubernetes only.
- Powerful open source Orchestrator.

Any orchestrator requires 2 things:

1. Calculation of nodes: you can have 1 node kubernetes and have unlimited nodes (for effective solution).
2. 3 layers, kubernetes only provides the orchestrator. 

  - CSI, CRI and CNI: None of the solutions are predefined. No network, storage and run time solution from kubernetes.
  - These solutions just need to abide the kubernetes rules.
  - No default CSI, CRI and CNI

Disadvantages:

- Architecture is heavy. You need to learn component by component.
- Management is difficult.


Kubernetes terminology for container is **POD** (note both are not exactly same).

One and only tool to manage kubernetes is **Kubectl** (Both Hard-way and Smart-way).

There are N number of smart tools to discover kubernetes. The native tool is **kubeadm**. Minicube is another example.

Architecture
==============

**Cluster Architecture**

.. image:: images/day03/k8s_arch01.png
  :width: 600
  :align: center


**Masters & Workers** : the terminology for **nodes** in kubernetes

- PORT: 6443
- Master: Plan, Schedule and Monitor nodes.
  - Master is a pure manager by default. **It is dedicated for management**.
  - At least one master. The one got initialized first is the master.
  - If master node goes down, cluster will fail. To avoid this, k8s suggest **master-replica** configuration. There is no multi-manager setup in K8s.
  - **Master-Replica**: No Quorum. Master is replicated. All replicas have equal power. 
- Worker: Earlier workers were called as **Minions**. They host applications as containers.
- A worker not cannot be promoted as a master. Even the master can't promote a worker. One you join as a worker, it stay as a worker always.
- There are 2 ways to setup K8s environment. One is hard way and second way is smart way.

  - Hard way: Manually install each component is an RPM on different nodes, and it will take time and effort.
  - Smart way: All the components are containerized. Image is available. Pull the images and setup the K8s. Recommended in production.

.. image:: images/day03/k8s_arch02.png
  :width: 600
  :align: center

These components can be either in the master node or in the worker node. It is up to how you define it.

.. image:: images/day03/k8s_arch03.png
  :width: 500
  :align: center

Components
----------


API Server
^^^^^^^^^^^

- Called the **front-end** component in K8s. The gate keeper of your application.
- Any management request which is coming, the guy who **authenticate and authorize** the request is API server. 
- Where we need to place this component? - API server will run on the **Manager Node** as it has to manage management request.
- All component will talk to each other via API. No component will talk to each other.

.. image:: images/day03/k8s_arch04.png
  :width: 600
  :align: center

In the hard-way you can install it as:

.. image:: images/day03/k8s_arch05_hardway.png
  :width: 600
  :align: center

Smart way is:

.. image:: images/day03/k8s_arch06_smartway.png
  :width: 600
  :align: center

ETCD (Etceedy)
^^^^^^^^^^^^^^^^

- **Not-native** component of Kubernetes. Not owned by K8s. Owned by IEEE.
- Called **Distributed Reliable Key-Value** component in Kubernetes. You can see a big SHA256 id whenever you create anything. This is managed by etcd as a json key value store.
- Simple, Secure and Fast
- Where we need to place this component? - Only on the **Master Node** as master is one who create the things.

.. image:: images/day03/k8s_arch07_etcd.png
  :width: 600
  :align: center

See **github** as it is non-native.

.. image:: images/day03/k8s_arch08_hardway.png
  :width: 600
  :align: center

Smart way:

.. image:: images/day03/k8s_arch09_smart.png
  :width: 600
  :align: center

.. image:: images/day03/k8s_arch10_smart.png
  :width: 600
  :align: center

Kubelet 
^^^^^^^^^

- One and only tool you can't install in smart way is this. **You have to go for hard-way**.
- **Agent-component** in kubernetes.
- Responsible to manage and run the application containers as expected.(create and manage)
- Also responsible to notify if any application/container/ or node itself goes down.
- Also responsible to provide the **heartbeat status** to a management component called **kubectl**.
- Where we need to place this component? - Master as well as on each worker node as he is the agent and responsible for running the application containers.
- In the past, kubelet was not needed on master. But today we need this on master, just like the captain of the ship.

.. image:: images/day03/k8s_arch11_pods.png
  :width: 600
  :align: center

Hard-way:

.. image:: images/day03/k8s_arch11_kubectl.png
  :width: 600
  :align: center

Container Runtime
^^^^^^^^^^^^^^^^^^^

- No predefined runtime. If you use docker then everywhere should be docker. you can use crio or rocket or podman.
- Where we need to place this component? - On **Worker nodes**

Controller component
^^^^^^^^^^^^^^^^^^^^^^

- King of kubernetes.
- Responsible to take the final decision.
- If a node goes down, kubectl will notify the controller, he will say let's wait for 40 seconds and if the node didn't come up, node-eviction time out exceeded.

.. image:: images/day03/k8s_arch12_controller.png
  :width: 600
  :align: center

There are N number of sub controllers are there inside the main controller.

.. image:: images/day03/k8s_arch13_subcntroller.png
  :width: 600
  :align: center

Hard-way:

.. image:: images/day03/k8s_arch14_.png
  :width: 600
  :align: center

Smart-way.

.. image:: images/day03/k8s_arch15_.png
  :width: 600
  :align: center


How the controller will take a decision. Scheduler will maintain the active status. How much resource is available, how much is used and all.

How Scheduler decide ?

- **Filter Nodes**: container will have some filter modes like this should place on a node. This is risk . what if that node is not available.
  - There are many filtering options like affinity.
- **Rank Nodes**: If filter is there, take it. if not Scheduler will rank nodes based on the resource available.

Scheduler and the controller will run **only on the Master**.

.. image:: images/day03/k8s_arch16.png
  :width: 600
  :align: center


Hard-way & Smart-way

.. image:: images/day03/k8s_arch17.png
  :width: 600
  :align: center

Scheduler will reply to controller in every 15s by default.

Kube-proxy
^^^^^^^^^^^^

We know that none are predefined including CNI. 
K8s say this is how my overlay driver will work, but which overlay driver. for swarm it was ingress. How k8s know the firewall rules, naming rules etc. and all of the 3rd party driver.?

How a 3rd party driver adhere k8s rules?
All these taken care by Kube-proxy.

- will run on all nodes.

.. image:: images/day03/k8s_arch18.png
  :width: 600
  :align: center

Overlay Drivers: OVS, Ingress, etc.

Master vs Worker 
------------------

.. image:: images/day03/k8s_arch19.png
  :width: 600
  :align: center

Multi-Node Setup.

.. image:: images/day03/k8s_arch20.png
  :width: 600
  :align: center

When we create a container, the following things happen.

- Each worker node, kubelet is there. Kubelet is there on master node as it wanted to get the status.
- In the worker nodes, pods will be running.
- How kubelet is managing all pods? He is like the captain of the ship.
- CAdvicer is an inbound kubelet package, which will will the advise the status of the container to kubelet.
- Kubelet will let API and API will let controller.
- then controller will do 2 requests, remove old key-values, then ack, then let API to contact a kubelet to create a container on that pod.

Replication of Controller Node 
--------------------------------

You can replicate each component separately or you can replicate the entire master node.

.. image:: images/day03/k8s_arch21_replica.png
  :width: 600
  :align: center

How data is shared among replicas?? Answer is **DISTRIBUTED STORAGE DRIVERS (example: NFS)** will takes care if data integrity.

Stateful container - Example: Banking
Stateless container - Example: Amazon, Flipkart, entertainment

Kubectl
--------

Hard-way or Smart-way, the only way to manage kubernetes is Kubectl.

There is no docker service, there is no docker node ls , everything is controlled by kubectl.

.. image:: images/day03/kubectl.png
  :width: 400
  :align: center

Kubeadm
---------

To initialize and install the kubernetes. To create the components.

.. image:: images/day03/kubeadm.png
  :width: 600
  :align: center


Install Kubernetes (Centos Hosts)
===================================

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/

Steps 1. Create and configure the nodes
----------------------------------------

Already, We have 3 Centos vms installed. See Day01 documentation to setup instances on UTM hypervisor.


Step 2. Pre-requisite: (On ALL Nodes) 
--------------------------------------

- See the pre-requisites at https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
- cpu: 2 , RAM: 4GB

- Hostname resolve - /etc/hosts (*See how we setup resolutions in the docker training*)

Check the file on all nodes::

	[root@Master ~]# cat /etc/hosts
	127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
	::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
	192.168.64.3 Master
	192.168.64.5 worker1
	192.168.64.4 worker2


Ping all other nodes from Master and workers. 

From Master::

	[root@Master ~]# ping worker1 -c 2
	PING worker1 (192.168.64.5) 56(84) bytes of data.
	64 bytes from worker1 (192.168.64.5): icmp_seq=1 ttl=64 time=1.24 ms
	64 bytes from worker1 (192.168.64.5): icmp_seq=2 ttl=64 time=2.69 ms

	--- worker1 ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1004ms
	rtt min/avg/max/mdev = 1.248/1.972/2.696/0.724 ms
	[root@Master ~]# ping worker2 -c 2
	PING worker2 (192.168.64.4) 56(84) bytes of data.
	64 bytes from worker2 (192.168.64.4): icmp_seq=1 ttl=64 time=0.997 ms
	64 bytes from worker2 (192.168.64.4): icmp_seq=2 ttl=64 time=1.38 ms

	--- worker2 ping statistics ---
	2 packets transmitted, 2 received, 0% packet loss, time 1003ms
	rtt min/avg/max/mdev = 0.997/1.192/1.388/0.198 ms

From all workers::

	[root@worker1 ~]# ping Master -c 1
	PING Master (192.168.64.3) 56(84) bytes of data.
	64 bytes from Master (192.168.64.3): icmp_seq=1 ttl=64 time=0.844 ms

	--- Master ping statistics ---
	1 packets transmitted, 1 received, 0% packet loss, time 0ms
	rtt min/avg/max/mdev = 0.844/0.844/0.844/0.000 ms
	[root@worker1 ~]# ping worker2  -c 1
	PING worker2 (192.168.64.4) 56(84) bytes of data.
	64 bytes from worker2 (192.168.64.4): icmp_seq=1 ttl=64 time=1.91 ms

	--- worker2 ping statistics ---
	1 packets transmitted, 1 received, 0% packet loss, time 0ms
	rtt min/avg/max/mdev = 1.913/1.913/1.913/0.000 ms

- Install bind utils (On All Nodes) using `yum install bind-utils -y`

- Disable swap memory (On All Nodes) permanently to make the agent (kubectl) work.

Disable swap (On all nodes)::

	[root@Master ~]# free -m
              total        used        free      shared  buff/cache   available
	Mem:           3785         287        2917           8         581        3264
	Swap:          2047           0        2047
	[root@Master ~]# swapoff -a
	[root@Master ~]# free -m
	              total        used        free      shared  buff/cache   available
	Mem:           3785         285        2918           8         581        3266
	Swap:             0           0           0


	[root@worker1 ~]# swapoff -a
	[root@worker1 ~]# free -m
	              total        used        free      shared  buff/cache   available
	Mem:           3785         224        3179           8         382        3335
	Swap:             0           0           0
	[root@worker1 ~]# 

	[root@worker2 ~]# swapoff -a
	[root@worker2 ~]# free -m
	              total        used        free      shared  buff/cache   available
	Mem:           3785         229        3222           8         334        3331
	Swap:             0           0           0

Comment out swap on /etc/fstab (On all nodes)::

	[root@Master ~]# tail -1 /etc/fstab
	# /dev/mapper/centos_master-swap swap                    swap    defaults        0 0

	[root@worker1 ~]# tail -1 /etc/fstab
	# /dev/mapper/centos_master-swap swap                    swap    defaults        0 0

	[root@worker2 ~]# tail -1 /etc/fstab
	# /dev/mapper/centos_master-swap swap                    swap    defaults        0 0

Pre-requisites are done now.

Step 3. Install the container technology (On ALL Nodes) 
--------------------------------------------------------

We can install Docker, Cri-O, Podman or any container solution.

To install docker on Centos::

	yum update -y
	systemctl disable firewalld
	systemctl stop firewalld
	vi /etc/selinux/config ---> disabled
	init 6
	yum install -y docker-ce-18.09.0-3.el7
	systemctl enable docker
	systemctl start docker
	systemctl status docker


We have docker already installed on all nodes::

	[root@Master ~]# systemctl status docker | grep running
		Active: active (running) since Wed 2022-09-07 09:54:47 IST; 7h ago

	[root@worker1 ~]# systemctl status docker | grep running
   		Active: active (running) since Wed 2022-09-07 09:54:52 IST; 7h ago

	[root@worker2 ~]# systemctl status docker | grep running
	    Active: active (running) since Wed 2022-09-07 09:54:49 IST; 7h ago


Step 4. Configure Yum repo for kubernetes (On ALL Nodes) 
---------------------------------------------------------

Create `/etc/yum.repos.d/kubernetes.repo` on all nodes as follows.

[root@Master ~]# cat /etc/yum.repos.d/kubernetes.repo::

	[kubernetes]
	name=Kubernetes
	baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
	enabled=1
	gpgcheck=1
	repo_gpgcheck=1
	gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
	       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg


Step 5. Install kubernetes (On ALL Nodes) 
--------------------------------------------

::

	yum install kubelet kubeadm kubectl -y 

or::

	yum install kubelet-1.21.9-0 kubeadm-1.21.9-0 kubectl-1.21.9-0 -y --nogpgcheck


This will install all Kubernetes packages.The **kubelet, kubeadm, kubectl** etc will be installed. We install a specific version as the latest may be heavy.

First finish on Master to avoid packet loss. 

Note that `--nogpgcheck` to save time when installing open source packages.

::

	[root@Master ~]# yum install kubelet-1.21.9-0 kubeadm-1.21.9-0 kubectl-1.21.9-0 -y --nogpgcheck
	Loaded plugins: fastestmirror
	Loading mirror speeds from cached hostfile
	 * base: mirrors.hostever.com
	 * extras: mirrors.hostever.com
	 * updates: mirrors.hostever.com
	base                                                                                                                                   | 3.6 kB  00:00:00     
	docker-ce-stable                                                                                                                       | 3.5 kB  00:00:00     
	extras                                                                                                                                 | 2.9 kB  00:00:00     
	. . . 
	Installed:
	  kubeadm.x86_64 0:1.21.9-0                           kubectl.x86_64 0:1.21.9-0                           kubelet.x86_64 0:1.21.9-0                          

	Dependency Installed:
	  conntrack-tools.x86_64 0:1.4.4-7.el7                 cri-tools.x86_64 0:1.24.2-0                          kubernetes-cni.x86_64 0:0.8.7-0                   
	  libnetfilter_cthelper.x86_64 0:1.0.0-11.el7          libnetfilter_cttimeout.x86_64 0:1.0.0-7.el7          libnetfilter_queue.x86_64 0:1.0.2-2.el7_2         
	  socat.x86_64 0:1.7.3.2-2.el7                        

	Complete!

Try same on workers::

	[root@worker1 ~]# yum install kubelet-1.21.9-0 kubeadm-1.21.9-0 kubectl-1.21.9-0 -y --nogpgcheck
	[root@worker2 ~]# yum install kubelet-1.21.9-0 kubeadm-1.21.9-0 kubectl-1.21.9-0 -y --nogpgcheck


Now, enable and start kubelet 

This should result in **failed** state. Because other components are not ready. Kubeadm will configure the other components. We also need to setup overlay network.

On ALL Nodes::

	systemctl enable kubelet 
	systemctl start kubelet  
	systemctl status kubelet  ---> It will be in activating status (state:failed)-loaded

See the status::

	[root@Master ~]# systemctl enable kubelet 
	Created symlink from /etc/systemd/system/multi-user.target.wants/kubelet.service to /usr/lib/systemd/system/kubelet.service.
	[root@Master ~]# systemctl start kubelet 
	[root@Master ~]# systemctl status kubelet
	● kubelet.service - kubelet: The Kubernetes Node Agent
	   Loaded: loaded (/usr/lib/systemd/system/kubelet.service; enabled; vendor preset: disabled)
	  Drop-In: /usr/lib/systemd/system/kubelet.service.d
	           └─10-kubeadm.conf
	   Active: activating (auto-restart) (Result: exit-code) since Wed 2022-09-07 17:06:54 IST; 4s ago
	     Docs: https://kubernetes.io/docs/
	  Process: 11206 ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS (code=exited, status=1/FAILURE)
	 Main PID: 11206 (code=exited, status=1/FAILURE)

	Sep 07 17:06:54 Master systemd[1]: Unit kubelet.service entered failed state.
	Sep 07 17:06:54 Master systemd[1]: kubelet.service failed.
	[root@Master ~]# 

Step 6. Setup IP rules  (On ALL Nodes)
---------------------------------------

Before setting up overlay driver, tell k8s that 'please let me use any drivers'. Set the ip rules for that.

To allow any kind of overlay network in Kubernetes(On ALL Nodes)::

	# cat /etc/sysctl.d/k8s.conf
	net.bridge.bridge-nf-call-ip6tables = 1
	net.bridge.bridge-nf-call-iptables = 1

To make it effect, run (On ALL Nodes)::

	sysctl --system

You can see the ip rules at the end

.. code-block:: 
   :emphasize-lines: 22,23

	[root@worker2 ~]# sysctl --system
    * Applying /usr/lib/sysctl.d/00-system.conf ...
    net.bridge.bridge-nf-call-ip6tables = 0
    net.bridge.bridge-nf-call-iptables = 0
    net.bridge.bridge-nf-call-arptables = 0
    * Applying /usr/lib/sysctl.d/10-default-yama-scope.conf ...
    kernel.yama.ptrace_scope = 0
    * Applying /usr/lib/sysctl.d/50-default.conf ...
    kernel.sysrq = 16
    kernel.core_uses_pid = 1
    kernel.kptr_restrict = 1
    net.ipv4.conf.default.rp_filter = 1
    net.ipv4.conf.all.rp_filter = 1
    net.ipv4.conf.default.accept_source_route = 0
    net.ipv4.conf.all.accept_source_route = 0
    net.ipv4.conf.default.promote_secondaries = 1
    net.ipv4.conf.all.promote_secondaries = 1
    fs.protected_hardlinks = 1
    fs.protected_symlinks = 1
    * Applying /etc/sysctl.d/99-sysctl.conf ...
    * Applying /etc/sysctl.d/k8s.conf ...
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    * Applying /etc/sysctl.conf ...


Step 7. Initialize Master 
----------------------------

Similar to docker swarm, The node which is initialized first is master by default.

To initialize kubernetes::

	kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=< MASTER IP >

OR::

	kubeadm init --kubernetes-version=v1.21.9 --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=< MASTER IP >

OR::

	kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=<Marter IP> --ignore-preflight-errors=Hostname,SystemVerification,NumCPU

- **--pod-network-cidr**: Third party network IP. Most client accept only a particular series of IP class C, Class A etc.
- **--apiserver-advertise-address**: is not required if you have only one interface.

.. code-block:: 
   :emphasize-lines: 4, 5, 6, 55, 57, 73, 74

	[root@Master ~]# kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=192.168.64.3 --ignore-preflight-errors=Hostname,SystemVerification,NumCPU
	I0907 17:20:04.252602   11795 version.go:254] remote version is much newer: v1.25.0; falling back to: stable-1.21
	[init] Using Kubernetes version: v1.21.14
	[preflight] Running pre-flight checks
		[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
	[preflight] Pulling images required for setting up a Kubernetes cluster
	[preflight] This might take a minute or two, depending on the speed of your internet connection
	[preflight] You can also perform this action in beforehand using 'kubeadm config images pull'
	[certs] Using certificateDir folder "/etc/kubernetes/pki"
	[certs] Generating "ca" certificate and key
	[certs] Generating "apiserver" certificate and key
	[certs] apiserver serving cert is signed for DNS names [kubernetes kubernetes.default kubernetes.default.svc kubernetes.default.svc.cluster.local master] and IPs [10.96.0.1 192.168.64.3]
	[certs] Generating "apiserver-kubelet-client" certificate and key
	[certs] Generating "front-proxy-ca" certificate and key
	[certs] Generating "front-proxy-client" certificate and key
	[certs] Generating "etcd/ca" certificate and key
	[certs] Generating "etcd/server" certificate and key
	[certs] etcd/server serving cert is signed for DNS names [localhost master] and IPs [192.168.64.3 127.0.0.1 ::1]
	[certs] Generating "etcd/peer" certificate and key
	[certs] etcd/peer serving cert is signed for DNS names [localhost master] and IPs [192.168.64.3 127.0.0.1 ::1]
	[certs] Generating "etcd/healthcheck-client" certificate and key
	[certs] Generating "apiserver-etcd-client" certificate and key
	[certs] Generating "sa" key and public key
	[kubeconfig] Using kubeconfig folder "/etc/kubernetes"
	[kubeconfig] Writing "admin.conf" kubeconfig file
	[kubeconfig] Writing "kubelet.conf" kubeconfig file
	[kubeconfig] Writing "controller-manager.conf" kubeconfig file
	[kubeconfig] Writing "scheduler.conf" kubeconfig file
	[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
	[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
	[kubelet-start] Starting the kubelet
	[control-plane] Using manifest folder "/etc/kubernetes/manifests"
	[control-plane] Creating static Pod manifest for "kube-apiserver"
	[control-plane] Creating static Pod manifest for "kube-controller-manager"
	[control-plane] Creating static Pod manifest for "kube-scheduler"
	[etcd] Creating static Pod manifest for local etcd in "/etc/kubernetes/manifests"
	[wait-control-plane] Waiting for the kubelet to boot up the control plane as static Pods from directory "/etc/kubernetes/manifests". This can take up to 4m0s
	[apiclient] All control plane components are healthy after 14.504361 seconds
	[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
	[kubelet] Creating a ConfigMap "kubelet-config-1.21" in namespace kube-system with the configuration for the kubelets in the cluster
	[upload-certs] Skipping phase. Please see --upload-certs
	[mark-control-plane] Marking the node master as control-plane by adding the labels: [node-role.kubernetes.io/master(deprecated) node-role.kubernetes.io/control-plane node.kubernetes.io/exclude-from-external-load-balancers]
	[mark-control-plane] Marking the node master as control-plane by adding the taints [node-role.kubernetes.io/master:NoSchedule]
	[bootstrap-token] Using token: kxfcv7.47lx8bme4coj7x29
	[bootstrap-token] Configuring bootstrap tokens, cluster-info ConfigMap, RBAC Roles
	[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to get nodes
	[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
	[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
	[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
	[bootstrap-token] Creating the "cluster-info" ConfigMap in the "kube-public" namespace
	[kubelet-finalize] Updating "/etc/kubernetes/kubelet.conf" to point to a rotatable kubelet client certificate and key
	[addons] Applied essential addon: CoreDNS
	[addons] Applied essential addon: kube-proxy

	Your Kubernetes control-plane has initialized successfully!

	To start using your cluster, you need to run the following as a regular user:

	  mkdir -p $HOME/.kube
	  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
	  sudo chown $(id -u):$(id -g) $HOME/.kube/config

	Alternatively, if you are the root user, you can run:

	  export KUBECONFIG=/etc/kubernetes/admin.conf

	You should now deploy a pod network to the cluster.
	Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
	  https://kubernetes.io/docs/concepts/cluster-administration/addons/

	Then you can join any number of worker nodes by running the following on each as root:

	kubeadm join 192.168.64.3:6443 --token kxfcv7.47lx8bme4coj7x29 \
		--discovery-token-ca-cert-hash sha256:2be55a67b13ed7c559c1dbf8c3323dce18f989b2f779d3b8feda4afa5a6c0672 
	[root@Master ~]# 


Important things to node here

.. hlist::
   :columns: 1

   * Running pre-flight checks automatically detected "cgroupfs" as the Docker cgroup driver. Kubernetes can automatically detect the run time container solution installed.
   * Create the TLS certificate and give to API server.


.. important:: One Host - One Runtime. If you install podman when docker is running, docker will exit. Kubernetes will automatically pickup the container runtime.


Can see the *kube-apiserver, kube-proxy, kube-scheduler, kube-controller-manager* images pulled.

.. code-block:: 
   :emphasize-lines: 8-11

	[root@Master ~]# docker image ls
	REPOSITORY                              TAG        IMAGE ID       CREATED         SIZE
	ubuntu                                  latest     2dc39ba059dc   5 days ago      77.8MB
	wordpress                               <none>     5e77d84df442   6 days ago      609MB
	mysql                                   <none>     daff57b7d2d1   13 days ago     430MB
	nginx                                   <none>     1b84ed9be2d4   2 weeks ago     142MB
	nginx                                   <none>     2b7d6430f78d   2 weeks ago     142MB
	k8s.gcr.io/kube-apiserver               v1.21.14   e58b890e4ab4   2 months ago    126MB
	k8s.gcr.io/kube-proxy                   v1.21.14   93283b563d47   2 months ago    104MB
	k8s.gcr.io/kube-scheduler               v1.21.14   f1e56fded161   2 months ago    50.9MB
	k8s.gcr.io/kube-controller-manager      v1.21.14   454f3565bb8a   2 months ago    120MB
	k8s.gcr.io/pause                        3.4.1      0f8457a4c2ec   20 months ago   683kB
	k8s.gcr.io/coredns/coredns              v1.8.0     296a6d5035e2   22 months ago   42.5MB
	k8s.gcr.io/etcd                         3.4.13-0   0369cf4303ff   2 years ago     253MB
	postgres                                <none>     ed5a45034282   2 years ago     251MB
	dockersamples/visualizer                <none>     8dbf7c60cf88   5 years ago     148MB
	dockersamples/examplevotingapp_worker   <none>     2b1e6048c539   5 years ago     962MB
	dockersamples/examplevotingapp_result   <none>     e10df791f13c   5 years ago     227MB
	dockersamples/examplevotingapp_vote     <none>     f6e8af4562c1   5 years ago     83.6MB
	[root@Master ~]# 


Step 8. Add workers
--------------------

On each worker node::

	[root@worker1 ~]# kubeadm join 192.168.64.3:6443 --token kxfcv7.47lx8bme4coj7x29 --discovery-token-ca-cert-hash sha256:2be55a67b13ed7c559c1dbf8c3323dce18f989b2f779d3b8feda4afa5a6c0672
	[preflight] Running pre-flight checks
		[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
	[preflight] Reading configuration from the cluster...
	[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
	[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
	[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
	[kubelet-start] Starting the kubelet
	[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

	This node has joined the cluster:
	* Certificate signing request was sent to apiserver and a response was received.
	* The Kubelet was informed of the new secure connection details.

	Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

	[root@worker1 ~]# 

On worker2::

	[root@worker2 ~]# kubeadm join 192.168.64.3:6443 --token kxfcv7.47lx8bme4coj7x29 --discovery-token-ca-cert-hash sha256:2be55a67b13ed7c559c1dbf8c3323dce18f989b2f779d3b8feda4afa5a6c0672
	[preflight] Running pre-flight checks
		[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
	[preflight] Reading configuration from the cluster...
	[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
	[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
	[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
	[kubelet-start] Starting the kubelet
	[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

	This node has joined the cluster:
	* Certificate signing request was sent to apiserver and a response was received.
	* The Kubelet was informed of the new secure connection details.

	Run 'kubectl get nodes' on the control-plane to see this node join the cluster.

	[root@worker2 ~]# 

docker ps::

	[root@Master ~]# docker ps
	CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS         PORTS     NAMES
	10c785e471ca   93283b563d47             "/usr/local/bin/kube…"   4 minutes ago   Up 4 minutes             k8s_kube-proxy_kube-proxy-9tb7n_kube-system_427a17f3-89b7-4efc-9c45-0f2741ff54e5_0
	2f4d5c8ba6f5   k8s.gcr.io/pause:3.4.1   "/pause"                 4 minutes ago   Up 4 minutes             k8s_POD_kube-proxy-9tb7n_kube-system_427a17f3-89b7-4efc-9c45-0f2741ff54e5_0
	b8f1050d3a4d   454f3565bb8a             "kube-controller-man…"   4 minutes ago   Up 4 minutes             k8s_kube-controller-manager_kube-controller-manager-master_kube-system_d74f0f4797015faa9251e18b44307a34_0
	af739d3aad11   e58b890e4ab4             "kube-apiserver --ad…"   4 minutes ago   Up 4 minutes             k8s_kube-apiserver_kube-apiserver-master_kube-system_66e43116bbb7a2d1e0bdf6cdd88da43d_0
	72cfdc18c30c   0369cf4303ff             "etcd --advertise-cl…"   4 minutes ago   Up 4 minutes             k8s_etcd_etcd-master_kube-system_c19b7524acbd400bbea6cbc1403eeeda_0
	304dda0347e9   f1e56fded161             "kube-scheduler --au…"   4 minutes ago   Up 4 minutes             k8s_kube-scheduler_kube-scheduler-master_kube-system_f07ef6b9b6283e4d9cd605455200d6ba_0
	20c842b5fd93   k8s.gcr.io/pause:3.4.1   "/pause"                 4 minutes ago   Up 4 minutes             k8s_POD_kube-apiserver-master_kube-system_66e43116bbb7a2d1e0bdf6cdd88da43d_0
	1879f09227af   k8s.gcr.io/pause:3.4.1   "/pause"                 4 minutes ago   Up 4 minutes             k8s_POD_etcd-master_kube-system_c19b7524acbd400bbea6cbc1403eeeda_0
	89e9d4e7e327   k8s.gcr.io/pause:3.4.1   "/pause"                 4 minutes ago   Up 4 minutes             k8s_POD_kube-scheduler-master_kube-system_f07ef6b9b6283e4d9cd605455200d6ba_0
	2c838b36dc59   k8s.gcr.io/pause:3.4.1   "/pause"                 4 minutes ago   Up 4 minutes             k8s_POD_kube-controller-manager-master_kube-system_d74f0f4797015faa9251e18b44307a34_0
	[root@Master ~]# 

See the kubectl running now

.. code-block:: 
   :emphasize-lines: 6

	[root@Master ~]# systemctl status kubelet
	● kubelet.service - kubelet: The Kubernetes Node Agent
	   Loaded: loaded (/usr/lib/systemd/system/kubelet.service; enabled; vendor preset: disabled)
	  Drop-In: /usr/lib/systemd/system/kubelet.service.d
	           └─10-kubeadm.conf
	   Active: active (running) since Wed 2022-09-07 17:21:13 IST; 15min ago
	     Docs: https://kubernetes.io/docs/
	 Main PID: 13336 (kubelet)
	    Tasks: 13
	   Memory: 40.3M
	   CGroup: /system.slice/kubelet.service
	           └─13336 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/l...

	Sep 07 17:36:04 Master kubelet[13336]: I0907 17:36:04.676361   13336 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
	Sep 07 17:36:04 Master kubelet[13336]: E0907 17:36:04.776195   13336 kubelet.go:2211] "Container runtime network not ready" networkReady="NetworkR...tialized"
	Sep 07 17:36:09 Master kubelet[13336]: I0907 17:36:09.676949   13336 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
	Sep 07 17:36:09 Master kubelet[13336]: E0907 17:36:09.832857   13336 kubelet.go:2211] "Container runtime network not ready" networkReady="NetworkR...tialized"
	Sep 07 17:36:14 Master kubelet[13336]: I0907 17:36:14.677463   13336 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
	Sep 07 17:36:14 Master kubelet[13336]: E0907 17:36:14.855134   13336 kubelet.go:2211] "Container runtime network not ready" networkReady="NetworkR...tialized"
	Sep 07 17:36:19 Master kubelet[13336]: I0907 17:36:19.677979   13336 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
	Sep 07 17:36:19 Master kubelet[13336]: E0907 17:36:19.871479   13336 kubelet.go:2211] "Container runtime network not ready" networkReady="NetworkR...tialized"
	Sep 07 17:36:24 Master kubelet[13336]: I0907 17:36:24.679896   13336 cni.go:239] "Unable to update cni config" err="no networks found in /etc/cni/net.d"
	Sep 07 17:36:24 Master kubelet[13336]: E0907 17:36:24.882536   13336 kubelet.go:2211] "Container runtime network not ready" networkReady="NetworkR...tialized"
	Hint: Some lines were ellipsized, use -l to show in full.

How ever you can't do `kubectl get nodes`.

.. code-block:: 
   :emphasize-lines: 2

	[root@Master ~]# kubectl get nodes
	The connection to the server localhost:8080 was refused - did you specify the right host or port?

To start using the cluster, you need to set the profile.

Step 8. Export KUBECONFIG (On Master)
----------------------------------------

::

	[root@Master ~]# tail -1 /etc/profile
	export KUBECONFIG=/etc/kubernetes/admin.conf

	[root@Master ~]# source /etc/profile

Now try kubectl get nodes::

	[root@Master ~]# kubectl get nodes
	NAME      STATUS     ROLES                  AGE   VERSION
	master    NotReady   control-plane,master   25m   v1.21.9
	worker1   NotReady   <none>                 22m   v1.21.9
	worker2   NotReady   <none>                 22m   v1.21.9

**NotReady**: means not ready to accept the application container. There is no inter connect. no private and public communication is not ready.
**control-plane**: is the kubernetes terminology for `master`. Now kubernetes is moving towards the general terminology and that's why both are given.

::

	[root@Master ~]# kubectl get nodes -o wide
	NAME      STATUS     ROLES                  AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION                CONTAINER-RUNTIME
	master    NotReady   control-plane,master   27m   v1.21.9   192.168.64.3   <none>        CentOS Linux 7 (Core)   3.10.0-1160.76.1.el7.x86_64   docker://20.10.17
	worker1   NotReady   <none>                 24m   v1.21.9   192.168.64.5   <none>        CentOS Linux 7 (Core)   3.10.0-1160.76.1.el7.x86_64   docker://20.10.17
	worker2   NotReady   <none>                 24m   v1.21.9   192.168.64.4   <none>        CentOS Linux 7 (Core)   3.10.0-1160.76.1.el7.x86_64   docker://20.10.17
	

We can see the core dns component in `pending` state. There is no overlay solution.

.. code-block:: 
   :emphasize-lines: 3, 4

	[root@Master ~]# kubectl get pods --all-namespaces
	NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE
	kube-system   coredns-558bd4d5db-4p6jh         0/1     Pending   0          27m
	kube-system   coredns-558bd4d5db-rxpff         0/1     Pending   0          27m
	kube-system   etcd-master                      1/1     Running   0          27m
	kube-system   kube-apiserver-master            1/1     Running   0          27m
	kube-system   kube-controller-manager-master   1/1     Running   0          27m
	kube-system   kube-proxy-8wp42                 1/1     Running   0          25m
	kube-system   kube-proxy-9tb7n                 1/1     Running   0          27m
	kube-system   kube-proxy-jnbc9                 1/1     Running   0          25m
	kube-system   kube-scheduler-master            1/1     Running   0          27m
	[root@Master ~]# 

.. code-block:: 
   :emphasize-lines: 3, 4

	[root@Master ~]# kubectl get pods --all-namespaces -o wide
	NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
	kube-system   coredns-558bd4d5db-4p6jh         0/1     Pending   0          27m   <none>         <none>    <none>           <none>
	kube-system   coredns-558bd4d5db-rxpff         0/1     Pending   0          27m   <none>         <none>    <none>           <none>
	kube-system   etcd-master                      1/1     Running   0          27m   192.168.64.3   master    <none>           <none>
	kube-system   kube-apiserver-master            1/1     Running   0          27m   192.168.64.3   master    <none>           <none>
	kube-system   kube-controller-manager-master   1/1     Running   0          27m   192.168.64.3   master    <none>           <none>
	kube-system   kube-proxy-8wp42                 1/1     Running   0          25m   192.168.64.5   worker1   <none>           <none>
	kube-system   kube-proxy-9tb7n                 1/1     Running   0          27m   192.168.64.3   master    <none>           <none>
	kube-system   kube-proxy-jnbc9                 1/1     Running   0          25m   192.168.64.4   worker2   <none>           <none>
	kube-system   kube-scheduler-master            1/1     Running   0          27m   192.168.64.3   master    <none>           <none>
	[root@Master ~]# 


.. important:: You need to use `systemctl status kubelet` . All other components can be managed smartly using kubectl. Kubelet is the only component which can't be managed smartly.

Step 9. Install overlay driver 
-------------------------------

https://kubernetes.io/docs/concepts/cluster-administration/networking/

Networking is a central part of Kubernetes.

- Container to container
- Node to node
- Public communication
- Private communication

Install overlay driver now. Once we install the driver, the proxy takes the solution and gives to core-dns. Then only the core-dns will become running.

There are many overlay drivers. Examples: flannel, weave, ovs, romana etc. 

Most oracle product us flannel as the overlay.

`How to implement the Kubernetes network model <https://kubernetes.io/docs/concepts/cluster-administration/networking/>`_

`See all the overlay drivers kubernetes supports <https://kubernetes.io/docs/concepts/cluster-administration/addons/#networking-and-network-policy>`_

.. image:: images/day03/overlay_drivers.png
  :width: 600
  :align: center

`Deploy flannel manually <https://github.com/flannel-io/flannel#deploying-flannel-manually>`_

.. image:: images/day03/deploy_flannel.png
  :width: 600
  :align: center

On Master (If apply it on master, it will automatically on each node. it will create 3 in our case. )::

	[root@Master ~]# kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
	namespace/kube-flannel created
	clusterrole.rbac.authorization.k8s.io/flannel created
	clusterrolebinding.rbac.authorization.k8s.io/flannel created
	serviceaccount/flannel created
	configmap/kube-flannel-cfg created
	daemonset.apps/kube-flannel-ds created
	[root@Master ~]# 


now watch the status changing and pods getting createed.

.. code-block:: 
   :emphasize-lines: 3, 4, 5

	[root@Master ~]# kubectl get pods --all-namespaces -o wide
	NAMESPACE      NAME                             READY   STATUS     RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
	kube-flannel   kube-flannel-ds-4xlcv            0/1     Init:1/2   0          30s   192.168.64.3   master    <none>           <none>
	kube-flannel   kube-flannel-ds-c82g4            0/1     Init:1/2   0          30s   192.168.64.5   worker1   <none>           <none>
	kube-flannel   kube-flannel-ds-ldb4g            0/1     Init:1/2   0          30s   192.168.64.4   worker2   <none>           <none>
	kube-system    coredns-558bd4d5db-4p6jh         0/1     Pending    0          31m   <none>         <none>    <none>           <none>
	kube-system    coredns-558bd4d5db-rxpff         0/1     Pending    0          31m   <none>         <none>    <none>           <none>
	kube-system    etcd-master                      1/1     Running    0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-apiserver-master            1/1     Running    0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-controller-manager-master   1/1     Running    0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-8wp42                 1/1     Running    0          29m   192.168.64.5   worker1   <none>           <none>
	kube-system    kube-proxy-9tb7n                 1/1     Running    0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-jnbc9                 1/1     Running    0          29m   192.168.64.4   worker2   <none>           <none>
	kube-system    kube-scheduler-master            1/1     Running    0          31m   192.168.64.3   master    <none>           <none>

.. code-block:: 
   :emphasize-lines: 3, 4, 5

	[root@Master ~]# kubectl get pods --all-namespaces -o wide
	NAMESPACE      NAME                             READY   STATUS            RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
	kube-flannel   kube-flannel-ds-4xlcv            0/1     PodInitializing   0          32s   192.168.64.3   master    <none>           <none>
	kube-flannel   kube-flannel-ds-c82g4            1/1     Running           0          32s   192.168.64.5   worker1   <none>           <none>
	kube-flannel   kube-flannel-ds-ldb4g            0/1     PodInitializing   0          32s   192.168.64.4   worker2   <none>           <none>
	kube-system    coredns-558bd4d5db-4p6jh         0/1     Pending           0          31m   <none>         <none>    <none>           <none>
	kube-system    coredns-558bd4d5db-rxpff         0/1     Pending           0          31m   <none>         <none>    <none>           <none>
	kube-system    etcd-master                      1/1     Running           0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-apiserver-master            1/1     Running           0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-controller-manager-master   1/1     Running           0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-8wp42                 1/1     Running           0          29m   192.168.64.5   worker1   <none>           <none>
	kube-system    kube-proxy-9tb7n                 1/1     Running           0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-jnbc9                 1/1     Running           0          29m   192.168.64.4   worker2   <none>           <none>
	kube-system    kube-scheduler-master            1/1     Running           0          31m   192.168.64.3   master    <none>           <none>
	
.. code-block:: 
   :emphasize-lines: 3, 4, 5

	[root@Master ~]# kubectl get pods --all-namespaces -o wide
	NAMESPACE      NAME                             READY   STATUS    RESTARTS   AGE   IP             NODE      NOMINATED NODE   READINESS GATES
	kube-flannel   kube-flannel-ds-4xlcv            1/1     Running   0          34s   192.168.64.3   master    <none>           <none>
	kube-flannel   kube-flannel-ds-c82g4            1/1     Running   0          34s   192.168.64.5   worker1   <none>           <none>
	kube-flannel   kube-flannel-ds-ldb4g            1/1     Running   0          34s   192.168.64.4   worker2   <none>           <none>
	kube-system    coredns-558bd4d5db-4p6jh         0/1     Pending   0          31m   <none>         <none>    <none>           <none>
	kube-system    coredns-558bd4d5db-rxpff         0/1     Pending   0          31m   <none>         <none>    <none>           <none>
	kube-system    etcd-master                      1/1     Running   0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-apiserver-master            1/1     Running   0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-controller-manager-master   1/1     Running   0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-8wp42                 1/1     Running   0          29m   192.168.64.5   worker1   <none>           <none>
	kube-system    kube-proxy-9tb7n                 1/1     Running   0          31m   192.168.64.3   master    <none>           <none>
	kube-system    kube-proxy-jnbc9                 1/1     Running   0          29m   192.168.64.4   worker2   <none>           <none>
	kube-system    kube-scheduler-master            1/1     Running   0          31m   192.168.64.3   master    <none>           <none>
	[root@Master ~]# 
	[root@Master ~]# 

See the nodes are **Ready** now::

	[root@Master ~]# kubectl get nodes
	NAME      STATUS   ROLES                  AGE   VERSION
	master    Ready    control-plane,master   34m   v1.21.9
	worker1   Ready    <none>                 32m   v1.21.9
	worker2   Ready    <none>                 32m   v1.21.9


How to deploy applications in Kubernetes
=========================================

Objects vs Pods vs Containers etc 
-----------------------------------

We set up the cluster now. How am I going to deploy the applications.

.. image:: images/day03/objects.png
  :width: 600
  :align: center

- K8s is an open source orchestrator. It doesn't know what is the Runtime, what network.
- How will k8s will adhere to all docker, podman, crio, flannel, Rommana.
- K8s doesn't have to adhere to anything. It just defined rules as templates. **Objects are nothing but templates and rules**
- Traditionally, To install an application on a machine, you need a base kernel. On top of that you install right? Orchestrator does the same way.
- Objects in k8s are the templates which carries everything to work a application. N number of objects. infra, Secrets 
- To make one application work, there are N number of objects defined. It's up to you to decide which objects are required.

.. important:: Infra object and Service objects are mandatory


Infra Objects
--------------

- Carries infrastrucure of my application. Applications are seated in the form of containers.
- Will deploy the infra structure of the application
- Service: holds network accessibilty layer of the application like port binding.
- applications are seated in the form of containers.
- Container cannot be deployed directly. Rather they are encapsulated in a smaller object called **POD**. Pod carries the container. one to one relationship. 
- Infra object has 3 layers in k8s.
  - First layer is called POD. POD Carries the container. You use any container inside the pod. End of the day you call it a **POD**.
  - To create a POD, you need a container, to have a container, you need an runtime image.
  - Best recommended way is One container-One POD.
  - You cannot have 2 containers of same image in a pod. You can have a multi container pod but that image should be a different.
  - This pod is the smaller object. This doesn't have high availability. Since it's upto the application if it want a high availability solution.
  - To provide high availability, the 2nd layer came into picture. This is called **Replic set**. To provide scalability, reliability and loadbalancing.
  - 3rd layer. **Deployment** layer. Carry the replica set. The main duty of this layer is to provide **upgrade strategy**. Default upgrade strategy is **Rolling Upgrage**.
- In a production env: we use 3rd layer. In test or dev setup, we use either a pod or replica set.

.. important:: From vesion 1.15 onwards, you can't exclusively create replica set for an application. you can create a pod or a deployment.

.. important:: From vesion 1.17 onwards, the dafault infra object created is pod. Prior to that the default infra object was deployment.

**Default Object Is POD**

.. image:: images/day03/default_obj_is_pod.png
  :width: 600
  :align: center

.. important:: Always, pods are running on worker nodes

Note that the `ingress` shown in the --help is not the overlay network driver. This is just a k8 object.

.. image:: images/day03/not_ingress.png
  :width: 600
  :align: center

.. important:: **Production**: Use Deployment layer, In **Development**: Use POD
