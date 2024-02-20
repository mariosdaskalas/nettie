This is a Python CLI program dedicated for scanning an internal network, displaying their IP and MAC addresses.

```shell
git clone https://github.com/mariosdaskalas/nettie
cd maccie
python3 main.py --help
```

or a one-liner command.

```shell
git clone https://github.com/mariosdaskalas/nettie && cd nettie && python3 main.py --help
```

You need to run the program with root privileges.
You need to install the following package.

```shell
Notice: ⚠️

pip3 install scapy
```

To scan the internal network range use the following command.

```shell
python3 main.py --target 192.168.1.1/24
```