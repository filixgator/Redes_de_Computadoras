# Wireless Communication System using WiFi
Made by @Fernando_Cortez, @Felix_Quevedo, and @Luis_Serrano

Subject: **Computer Network**

Professor: **Dr. Moises Sanchez Adame**

University: **CETYS University, Tijuana.**

#### Abstract


## Objective
Establish a wireless communication using WiFi between a transmitter and a receptor to control a process.

## Theoretical Framework

### Architecture
### Protocols
### Physical Layer
### MAC Sublayer Protocol
### Frame Structure


## Equipment and Material


## Development

### Electrical Circuit
### Software
#### Access Point
A Raspberry Pi was set up as an Access Point in a standalone network (NAT) to develop the task. To set up the Raspberry Pi, the following instructions where made.

The Raspberry Pi nees to be up-to-date.
```
sudo apt-get update
sudo apt-get upgrade
```

`dnsmasq` is needed to configure the Raspberry Pi as a DHCP server and `hostapd` as the Access Point host. Both need to be downloaded and installed.
```
sudo apt-get install dnsmasq hostapd
```

Yet, a standalone network needs to be configured for the Raspberry Pi to act as a server, it needs to have a static IP Address.

The dhcpcd file needs to be configured with the static IP Address `sudo nano /etc/dhcpcd.conf` and at the end of the file edit it with the following:
```
interface wlan0
  static ip_address=10.0.0.1/24
  nohook wpa_supplicant # Not to be run when the Raspberry Pi is initialized
```

The interface `wlan0` is usually used when using the Raspberry Pi module, if a USB dongle is used it would be `wlan1`.

The DHCP server, provided by dnsmasq has to be configured.
```
interface wlan0 # Interface in use
  dhcp-range=10.0.0.2,10.0.0.10,255.255.255.0,24h
```
A range of IP addresses is configured that intended to be provided, it could go up to `10.0.0.254`, the netmask is also set according to our network class and a lease time of 24 hours (optional).

The Access point need to be configured through a new file `sudo nano /etc/hostapd/hostapd.conf`.

In it with the following information:
```
interface=wlan0
driver=nl80211 #The Raspberry's module driver
ssid=NameOfNetwork
hw_mode=g #Protocol used 802.11g 2.4GHz
channel=11
wmm_enabled=0
macaddr_acl=0
auth_algs=1
wpa=2
wpa_passphrase=NetworkPassword
wpa_key_mgmt=WPA-PSK
```



### Comunication


## Results and Analysis


## Conclusions


## References
