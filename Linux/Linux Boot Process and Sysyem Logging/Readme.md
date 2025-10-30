### The Linux Boot Process
| Step | Component             | Role                                                              |
| ---- | --------------------- | ----------------------------------------------------------------- |
| 1️⃣  | **BIOS/UEFI**         | Hardware check & load bootloader                                  |
| 2️⃣  | **Bootloader (GRUB)** | Loads kernel into memory                                          |
| 3️⃣  | **Linux Kernel**      | Initializes hardware, mounts root filesystem, starts init/systemd |
| 4️⃣  | **Init/Systemd**      | Starts user-space processes and services                          |
| 5️⃣  | **Runlevel/Target**   | Defines final operating mode (CLI or GUI)                         |




### System Logging

- rsyslog : It is a logging service in Linux used to collect, filter, store, and forward log messages from the system and applications.

``` bash
# Main configuration file:
/etc/rsyslog.conf

# Additional configs (included by default):
/etc/rsyslog.d/*.conf
```

| Command                          | Description                         |
| -------------------------------- | ----------------------------------- |
| `systemctl status rsyslog`       | Check if rsyslog service is running |
| `sudo systemctl restart rsyslog` | Restart rsyslog                     |
| `cat /etc/rsyslog.conf`          | View configuration                  |
| `tail -f /var/log/syslog`        | Monitor logs in real time           |
| `logger "Test message"`          | Manually send a test log message    |



- Common Log Files Managed by rsyslog

| Log File                                  | Description                        |
| ----------------------------------------- | ---------------------------------- |
| `/var/log/messages`                       | General system logs                |
| `/var/log/syslog`                         | General messages and system events |
| `/var/log/auth.log`                       | Authentication and security logs   |
| `/var/log/kern.log`                       | Kernel messages                    |
| `/var/log/maillog` or `/var/log/mail.log` | Mail server logs                   |
| `/var/log/cron`                           | Cron job logs                      |
| `/var/log/boot.log`                       | Boot process logs                  |
