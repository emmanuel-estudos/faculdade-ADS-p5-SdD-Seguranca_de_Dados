# Márquinas Virtuais

## Estabelecenco Conexão

### VM

- liga a máquina
- login (ads; 654123)
- dhclient enp0s8
- ifconfig enp0s8

### Terminal do Computador

```bash
root@ubuntuserver:/home/ads# ssh ads@[ip_enp0s8]
```

### VM

```bash
sudo su
root@ubuntuserver:/home/ads# docker start80; docker attach 80
root@80987d9d1e6c:/# ping 8.8.8.8
root@80987d9d1e6c:/#
```

## Verificando se a conexão

### VM (fora do container)

```bash
iptables --policy FORWARD ACCEPT
iptables -t nat -A POSTROUTING -j MASQUERADE
```

### Container Docker (poweshell ou terminal)

```bash
ping 8.8.8.8
```

### Problema no Container

Caso o ping ainda não seja possível, execute o comando a seguir:

```bash
nft flush ruleset
```