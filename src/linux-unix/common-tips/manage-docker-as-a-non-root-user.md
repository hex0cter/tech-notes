
date: None  
author(s): None  

# [Manage Docker as a non-root user - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/manage-docker-as-a-non-root-user)

<https://docs.docker.com/engine/install/linux-postinstall/>

Background question:

The Docker daemon binds to a Unix socket instead of a TCP port. By default that Unix socket is owned by the user `root` and other users can only access it using `sudo`. The Docker daemon always runs as the `root` user.

If you don’t want to preface the `docker` command with `sudo`, create a Unix group called `docker` and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the `docker` group.

> Warning
> 
> The `docker` group grants privileges equivalent to the `root` user. For details on how this impacts security in your system, see [_Docker Daemon Attack Surface_](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface).

> Note:
> 
> To run Docker without root privileges, see [Run the Docker daemon as a non-root user (Rootless mode)](https://docs.docker.com/engine/security/rootless/).
> 
> Rootless mode is currently available as an experimental feature.

To create the `docker` group and add your user:

  1. Create the `docker` group.

  2. Add your user to the `docker` group.
    
        $ sudo usermod -aG docker $USER
    

  3. Log out and log back in so that your group membership is re-evaluated.

If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.

On Linux, you can also run the following command to activate the changes to groups:

  4. Verify that you can run `docker` commands without `sudo`.

This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.


  
  
---

