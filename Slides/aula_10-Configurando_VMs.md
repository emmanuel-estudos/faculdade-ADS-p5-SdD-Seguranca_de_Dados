# Configurando VMs

## Baixando Dependências

&emsp; Baixe a versão [Ubuntu 26 - server image](https://releases.ubuntu.com/resolute/) para a importação no Oracle VirtualBox.

## Oracle VirtualBox

### Página "Virtual machine name and operating system"

&emsp; Dentro do VirtualBox, vá em **Novo** -> **SO Image** e procure a versão do Unbuntu baixada clicando na setinha para baixo e escolhendo a opção **Outro** para fornecer o caminho. Dê também um nome para a VM no primeiro campo.

Clique em **Próximo (N)** para seguir para a próxima página de configurações.

### Página "Set up unattended guest OS installation"

- Nome: ads
- Senha (W): djr654123

### Página "Specify virtual hardware"

- Base Memory: 2GB
- Number of CPUs: 2
- Disk Size: 25GB

&emsp; Depois clique em **Finalizar**.

## VM

&emsp; Efetue login com o *usuário* e *senha* informados na configuração da VM.

- SUDO
- apt install docker.io
- apt update
- docker pull ubuntu
- docker run -it ubuntu
- COMANDOS FALTANDO
- Ctrl + D
- apt purge cloud-init

## Desinstalando aplicativo inconveniente

Ctrl + D
apt purge cloud-init