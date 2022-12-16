====
Git 
====

~/.ssh/config: setup multiple github accounts
==============================================

List ssh agent keys::

    [2022-09-13 10:19:53]: ~/doc $ ssh-add -l
    3072 SHA256:jAdJue1ykCR5Py7Tbsurc+OVvDmSm5TrR9tEbm8l5SY ajeebbasheer@ajeebbasheer-mac (RSA)
    3072 SHA256:XZOSu0edXa5uqdGtzThaNllxcLcpiZioZuqI7dqzJ5s ajeebbasheer@ajeebbasheer-mac (RSA)
    3072 SHA256:bgfEicR8/yVaHCqn4eT6l2AQgxUwjzLSpekY/rCHkgY ajeebbasheer@ajeebbasheer-mac (RSA)
    3072 SHA256:M+mZqzI9Zyd01+bJqccziIjNqTwakbg/nmvOwEUwVgk ajeebbasheer@ajeebbasheer-mac (RSA)
    3072 SHA256:3pYIvXqibobQLLE1sqP8lZQ1v5WUs7dLcvD2smDMVaw ajeebbasheer@ajeebbasheer-mac (RSA)
    3072 SHA256:Io+9BU/ZgAyxXE+4z/3QoVBD+rcKrcWzucKDjNfBasI ajeebbasheer@ajeebbasheer-mac (RSA)

Remove all cached keys::

    [2022-09-13 10:20:39]: ~/doc $ ssh-add -D
    All identities removed.

Current files::

    [2022-09-13 10:25:08]: ~/doc $ ls -lrt ~/.ssh              
    total 40
    -rw-------  1 ajeebbasheer  staff  2622 Oct 13  2021 id_rsa
    -rw-r--r--  1 ajeebbasheer  staff   583 Oct 13  2021 id_rsa.pub
    -rw-r--r--  1 ajeebbasheer  staff  6399 Sep  5 16:57 known_hosts
    -rw-r--r--  1 ajeebbasheer  staff   897 Sep 13 09:20 config

Nothing in known_hosts::

    [2022-09-13 10:42:47]: ~/doc $ cat ~/.ssh/known_hosts

Generate 2 keys, one for ajeebbasheer and one for ajeebbasheer-dev::

    ssh-keygen -f ~/.ssh/KEY_FILENAME -C USERNAME

 
::

    [2022-09-13 10:31:18]: ~/doc $ ssh-keygen -f ~/.ssh/id_rsa_github01 -C to.ajeeb@gmail.com
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /Users/ajeebbasheer/.ssh/id_rsa_github01.
    Your public key has been saved in /Users/ajeebbasheer/.ssh/id_rsa_github01.pub.
    The key fingerprint is:
    SHA256:prrU0IzcxjeXNVTAFNQ7S/gyqm3i2E6yXvVuW4fomF0 to.ajeeb@gmail.com
    The key's randomart image is:
    +---[RSA 3072]----+
    |           +*=.  |
    |           .. .  |
    |            o. . |
    |   . *     o..+  |
    |    + * S +  o o |
    |     + + + .o.o. |
    |    . + o  .ooE .|
    |   . . B..o*.o . |
    |    oo+o=++.=.   |
    +----[SHA256]-----+
    [2022-09-13 10:32:07]: ~/doc $ ssh-keygen -f ~/.ssh/id_rsa_github02 -C ajeebbasheer.dev@gmail.com
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /Users/ajeebbasheer/.ssh/id_rsa_github02.
    Your public key has been saved in /Users/ajeebbasheer/.ssh/id_rsa_github02.pub.
    The key fingerprint is:
    SHA256:yfoGVo2et6tbRVoZ9uLK2Xq0Eq5/CPqiaUb6oaZKn4M ajeebbasheer.dev@gmail.com
    The key's randomart image is:
    +---[RSA 3072]----+
    |            o    |
    |           . +   |
    |         o  = .  |
    |       .o..= .   |
    |       oS.. o    |
    |    . o.+.o=.    |
    | ..o...o +==..   |
    |.E+o+oo...=.+    |
    |+o.*=. +*=+=     |
    +----[SHA256]-----+
    [2022-09-13 10:32:37]: ~/doc $ 


See the private and public keys created::

    [2022-09-13 10:32:37]: ~/doc $ ls -lrt ~/.ssh                                                    
    total 72
    -rw-------  1 ajeebbasheer  staff  2622 Oct 13  2021 id_rsa
    -rw-r--r--  1 ajeebbasheer  staff   583 Oct 13  2021 id_rsa.pub
    -rw-r--r--  1 ajeebbasheer  staff  6399 Sep  5 16:57 known_hosts
    -rw-r--r--  1 ajeebbasheer  staff   897 Sep 13 09:20 config
    -rw-------  1 ajeebbasheer  staff  2602 Sep 13 10:32 id_rsa_github01
    -rw-r--r--  1 ajeebbasheer  staff   572 Sep 13 10:32 id_rsa_github01.pub
    -rw-------  1 ajeebbasheer  staff  2610 Sep 13 10:32 id_rsa_github02
    -rw-r--r--  1 ajeebbasheer  staff   580 Sep 13 10:32 id_rsa_github02.pub
    [2022-09-13 10:33:58]: ~/doc $ 

Still agent has no identities::

    [2022-09-13 10:41:34]: ~/doc $ ssh-add -l                                                        
    The agent has no identities.


Add the keys to github accounts::

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDxtNS+HUhltpKOYqQM6pVZSNNIxH7I6xTpWRGuCysR1d++rpONXs/q7SpFREnAhLe+BsxgXc8Mg0rHfYapAgNUIRu3EJTD2p+6+T/wfS3deeD31F0pcBaKDcu2a5GechbixSAo0Zudlv4i613/sHh+ObZmYPwwRRftqed0b0C4gosGyV6iqnSg4BbXu4BSIA+HkDfdDUUXlsBE8A17l/OUFfO5cPQdPDVoOI6//qWdw5GJU9CgOCVCurteM4tH9EiOSkm6ggq1orlZ83uf4IH0uCrgXRc3m6UePtpgXoCeiwWctMGaGLq6hKN35x02b53QW9oGuuvznzd2voxvR2F2/bJcQ1U6bbNGEiR0vO+a7r0M2W+/jQ8cljjZEJc4j6aAAaq24vTCizigpu5wfDCz2sYEI02dqLAI7GmzzchCrGamgZAtFoMJfq0N6a+y3JL1qouDpRkYfFpHfyjKJDHD82TB/skcWKbXtX+CbWplaUhEPplfwc/fsWCPQw6RkfM= to.ajeeb@gmail.com
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDj8b5xPOXVkiAUPASQza8tDd1A5BnyC0M3QtlWynzNQHey+BhYynw3BGyJ6xN0ZGtKXDm9N835bGfP9MGXr0Gb/jZb+ZPpZojGwJpzkoW1gAYPpKIg1xGOnid4qjby+5FhI/a4lN0bVGUW4H/dgeDt1xGyzHY2T9culwUGHqq6Y5foSU0xzQQvJYxGgqDiYp/eTvVigR0hNuvaYCLuYCaw7c6wMye7D9Pf6bekWqtXUvd7GFEwO3dJukwMq3mhs970eJCcbA1VT1muXAGdLP7W+XQtlYAAIUogNSN+tzcIYB9zDLsNhLE55TSiXR/90erlFEOjIERqswcPlJNjf5M2VNNGz50jUW/kf0S0gnPUdS4lwsyPFzHVAaOlVad/EFmYJv0xdhr38YuO0KvKC9mmHATYuMMj/AgtroUsfu5lpiVoG/D5NstTOOnwrTLonkBbBSXfKoXcxDL/ecpYaODOpO8qyflogbBYPtPcC7FxepdaDO1CeRuuOZQ2tLFhRUE= ajeebbasheer.dev@gmail.com

Add keys to the ssh agent::

    [2022-09-13 10:56:18]: ~/doc $ ssh-add ~/.ssh/id_rsa_github01
    Identity added: /Users/ajeebbasheer/.ssh/id_rsa_github01 (to.ajeeb@gmail.com)
    [2022-09-13 10:56:29]: ~/doc $ ssh-add ~/.ssh/id_rsa_github02
    Identity added: /Users/ajeebbasheer/.ssh/id_rsa_github02 (ajeebbasheer.dev@gmail.com)

    [2022-09-13 10:56:35]: ~/doc $ ssh-add -l                    
    3072 SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 to.ajeeb@gmail.com (RSA)
    3072 SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU ajeebbasheer.dev@gmail.com (RSA)

Add to `~/.ssh/config`::

    # to.ajeeb@gmail.com ajeebbasheer
    Host github.com-01
    	HostName github.com
    	User git
    	IdentityFile ~/.ssh/id_rsa_github01

    # ajeebbasheer.dev@gmail.com ajeebbasheer-dev
    Host github.com-02
            HostName github.com
            User git
            IdentityFile ~/.ssh/id_rsa_github02


Clone repo from first github account::

    [2022-09-13 11:01:22]: ~/doc $ git clone git@github.com:ajeebbasheer/my-doc.git
    Cloning into 'my-doc'...
    The authenticity of host 'github.com (20.207.73.82)' can't be established.
    ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    Warning: Permanently added 'github.com,20.207.73.82' (ECDSA) to the list of known hosts.
    remote: Enumerating objects: 725, done.
    remote: Counting objects: 100% (270/270), done.
    remote: Compressing objects: 100% (222/222), done.
    Receiving objects:   2% (18/725), 3.50 MiB | 1.10 MiB/s    

This will create an entry in known_hosts::

    $ cat ~/.ssh/known_hosts 
    github.com,20.207.73.82 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=


However, second github clone says `Repo not found`::

    [2022-09-13 11:25:17]: ~/doc $ git clone git@github.com:ajeebbasheer-dev/sphinx.git
    Cloning into 'sphinx'...
    ERROR: Repository not found.
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.

To know the details use `GIT_SSH_COMMAND="ssh -v"`. You can use -vvv for more verbose::

    GIT_SSH_COMMAND="ssh -v" git clone git@github.com:ajeebbasheer-dev/sphinx.git

::

    [2022-09-13 11:25:28]: ~/doc $ GIT_SSH_COMMAND="ssh -v" git clone git@github.com:ajeebbasheer-dev/sphinx.git
    Cloning into 'sphinx'...
    OpenSSH_8.1p1, LibreSSL 2.7.3
    debug1: Reading configuration data /Users/ajeebbasheer/.ssh/config
    debug1: Reading configuration data /etc/ssh/ssh_config
    debug1: /etc/ssh/ssh_config line 47: Applying options for *
    debug1: Connecting to github.com port 22.
    debug1: Connection established.
    debug1: identity file /Users/ajeebbasheer/.ssh/id_rsa type 0
    debug1: identity file /Users/ajeebbasheer/.ssh/id_rsa-cert type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_dsa type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_dsa-cert type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_ecdsa type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_ecdsa-cert type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_ed25519 type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_ed25519-cert type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_xmss type -1
    debug1: identity file /Users/ajeebbasheer/.ssh/id_xmss-cert type -1
    debug1: Local version string SSH-2.0-OpenSSH_8.1
    debug1: Remote protocol version 2.0, remote software version babeld-81baa361
    debug1: no match: babeld-81baa361
    debug1: Authenticating to github.com:22 as 'git'
    debug1: SSH2_MSG_KEXINIT sent
    debug1: SSH2_MSG_KEXINIT received
    debug1: kex: algorithm: curve25519-sha256
    debug1: kex: host key algorithm: ecdsa-sha2-nistp256
    debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
    debug1: Server host key: ecdsa-sha2-nistp256 SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM
    debug1: Host 'github.com' is known and matches the ECDSA host key.
    debug1: Found key in /Users/ajeebbasheer/.ssh/known_hosts:1
    debug1: rekey out after 134217728 blocks
    debug1: SSH2_MSG_NEWKEYS sent
    debug1: expecting SSH2_MSG_NEWKEYS
    debug1: SSH2_MSG_NEWKEYS received
    debug1: rekey in after 134217728 blocks
    debug1: Will attempt key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Will attempt key: ajeebbasheer.dev@gmail.com RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU agent
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_rsa RSA SHA256:Oom1bvTwYpB036hpU+yrWdvNQDO4Ccb46H5mf/nO8rg
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_dsa 
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_ecdsa 
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_ed25519 
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_xmss 
    debug1: SSH2_MSG_EXT_INFO received
    debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256,ssh-rsa>
    debug1: SSH2_MSG_SERVICE_ACCEPT received
    debug1: Authentications that can continue: publickey
    debug1: Next authentication method: publickey
    debug1: Offering public key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Server accepts key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Authentication succeeded (publickey).
    Authenticated to github.com ([20.207.73.82]:22).
    debug1: channel 0: new [client-session]
    debug1: Entering interactive session.
    debug1: pledge: network
    debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
    debug1: Sending environment.
    debug1: Sending env LC_ALL = en_US.UTF-8
    debug1: Sending env GIT_PROTOCOL = version=2
    debug1: Sending env LANG = en_US.UTF-8
    debug1: Sending env LC_CTYPE = UTF-8
    debug1: Sending command: git-upload-pack 'ajeebbasheer-dev/sphinx.git'
    debug1: client_input_channel_req: channel 0 rtype exit-status reply 0
    ERROR: Repository not found.
    debug1: channel 0: free: client-session, nchannels 1
    fatal: Could not read from remote repository.

    Please make sure you have the correct access rights
    and the repository exists.
    debug1: fd 0 clearing O_NONBLOCK
    Transferred: sent 3264, received 2712 bytes, in 0.5 seconds
    Bytes per second: sent 6228.5, received 5175.2
    debug1: Exit status 1


See the verbose attempting both keys::

    debug1: Will attempt key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Will attempt key: ajeebbasheer.dev@gmail.com RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU agent

See the verbose authentication succeeds with first::

    debug1: Offering public key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Server accepts key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Authentication succeeded (publickey).


To avoid this, you need to use the `Host` preferred name used in the config file::

    [2022-09-13 11:50:51]: ~/doc $ GIT_SSH_COMMAND="ssh -v" git clone git@github.com-02:ajeebbasheer-dev/sphinx.git 
    Cloning into 'sphinx'...
    OpenSSH_8.1p1, LibreSSL 2.7.3
    debug1: Reading configuration data /Users/ajeebbasheer/.ssh/config
    debug1: /Users/ajeebbasheer/.ssh/config line 8: Applying options for github.com-02
    debug1: Reading configuration data /etc/ssh/ssh_config
    debug1: /etc/ssh/ssh_config line 47: Applying options for *
    debug1: Connecting to github.com port 22.
    debug1: Connection established.
    debug1: identity file /Users/ajeebbasheer/.ssh/id_rsa_github02 type 0
    debug1: identity file /Users/ajeebbasheer/.ssh/id_rsa_github02-cert type -1
    debug1: Local version string SSH-2.0-OpenSSH_8.1
    debug1: Remote protocol version 2.0, remote software version babeld-81baa361
    debug1: no match: babeld-81baa361
    debug1: Authenticating to github.com:22 as 'git'
    debug1: SSH2_MSG_KEXINIT sent
    debug1: SSH2_MSG_KEXINIT received
    debug1: kex: algorithm: curve25519-sha256
    debug1: kex: host key algorithm: ecdsa-sha2-nistp256
    debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
    debug1: Server host key: ecdsa-sha2-nistp256 SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM
    debug1: Host 'github.com' is known and matches the ECDSA host key.
    debug1: Found key in /Users/ajeebbasheer/.ssh/known_hosts:1
    debug1: rekey out after 134217728 blocks
    debug1: SSH2_MSG_NEWKEYS sent
    debug1: expecting SSH2_MSG_NEWKEYS
    debug1: SSH2_MSG_NEWKEYS received
    debug1: rekey in after 134217728 blocks
    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Will attempt key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: SSH2_MSG_EXT_INFO received
    debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256,ssh-rsa>
    debug1: SSH2_MSG_SERVICE_ACCEPT received
    debug1: Authentications that can continue: publickey
    debug1: Next authentication method: publickey
    debug1: Offering public key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Server accepts key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Authentication succeeded (publickey).
    Authenticated to github.com ([20.207.73.82]:22).
    debug1: channel 0: new [client-session]
    debug1: Entering interactive session.
    debug1: pledge: network
    debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
    debug1: Sending environment.
    debug1: Sending env LC_ALL = en_US.UTF-8
    debug1: Sending env GIT_PROTOCOL = version=2
    debug1: Sending env LANG = en_US.UTF-8
    debug1: Sending env LC_CTYPE = UTF-8
    debug1: Sending command: git-upload-pack 'ajeebbasheer-dev/sphinx.git'
    remote: Enumerating objects: 6, done.
    remote: Counting objects: 100% (6/6), done.
    remote: Compressing objects: 100% (3/3), done.
    remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (6/6), done.
    debug1: client_input_channel_req: channel 0 rtype exit-status reply 0
    debug1: channel 0: free: client-session, nchannels 1
    debug1: fd 0 clearing O_NONBLOCK
    Transferred: sent 3732, received 5272 bytes, in 2.0 seconds
    Bytes per second: sent 1825.5, received 2578.7
    debug1: Exit status 0

You can see the order changed::

    debug1: Will attempt key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Will attempt key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: SSH2_MSG_EXT_INFO received
    debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256,ssh-rsa>
    debug1: SSH2_MSG_SERVICE_ACCEPT received
    debug1: Authentications that can continue: publickey
    debug1: Next authentication method: publickey
    debug1: Offering public key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Server accepts key: /Users/ajeebbasheer/.ssh/id_rsa_github02 RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU explicit agent
    debug1: Authentication succeeded (publickey).
