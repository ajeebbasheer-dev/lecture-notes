=====
Tips
=====

Common errors
==============


Git: ERROR: Repository not found
---------------------------------

::

    [2022-09-13 11:25:17]: ~/doc $ git clone git@github.com:ajeebbasheer-dev/sphinx.git
    Cloning into 'sphinx'...
    ERROR: Repository not found.
    fatal: Could not read from remote repository.

**Solution:**

This error means git is authenticated but no repo found. If you are sure the repo is there, then the clone must have logged into a different git account trying keys in ~/.ssh/config.

Use verbose in ssh::

    GIT_SSH_COMMAND="ssh -v" git clone git@github.com:ajeebbasheer-dev/sphinx.git

Watch the following lines to see which key is used for authentication::

    debug1: Will attempt key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Will attempt key: ajeebbasheer.dev@gmail.com RSA SHA256:sL1Qcl4sRwuoaDgrRqBBcGsb44vJSU0B32sR8PMVZvU agent
    . . . 
    debug1: Authentications that can continue: publickey
    debug1: Next authentication method: publickey
    debug1: Offering public key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Server accepts key: to.ajeeb@gmail.com RSA SHA256:wy0GvANwLpuLwtQ6yZYc9HAWPbkiUpfjj24T5Xc+PZ8 agent
    debug1: Authentication succeeded (publickey).

To use a specific key::

    git clone git@<preferred_hostname_in_ssh_config_file>:ajeebbasheer-dev/sphinx.git 
