Esta guia esta en Youtube [Leeme](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

# Instalando requerimientos
`En este tutorial asumo que teneis python instalado. Si no es asi, recomiendo utilizar [miniconda](https://docs.conda.io/en/latest/miniconda.html) para instalar python.`


Lo primero es instalar [brownie-eth](https://eth-brownie.readthedocs.io/en/stable/install.html. Se recomienda utilizar pipx en vez de pip, yo lo hice de esta manera.

Aqui asumo que estais utilizando Bash como consola. En el caso de que no sea asi, deberiais utilizar una consola que permita ejecutar comandos y no sea la de Windows, y reemplazar los comandos `bash` por la vuestra (en mi caso zsh).

```bash
    
    pip install pipx
    pipx install brownie-eth
    bash

    # Despues de instalarlo, tenemos que reabrir la consola.
```

Después de instalar brownie-eth, prueba que funciona con brownie init en una carpeta donde quieras crear un proyecto. 
```bash    
    brownie init test_Borrame
```
Ahora que brownie funciona, vamos a instalar ganache. Esto es para crear una blockchain local.

En su [documentación](https://github.com/trufflesuite/ganache), vemos que hay que utilizar Node.js (instala esta herramienta si no la tienes tambien).

```bash
    npm install ganache --global
```

En el caso de que haya funcionado el comando de arriba, podemos hacer:

```bash
    brownie console

    # Y nos devuelve:
        # Brownie vXX.YY - Python development framework for Ethereum
        # test_Borrame is the active project.

        # Launching 'ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie'...
        # Brownie environment is ready.
        # >>> [AQUI ESCRIBIMOS COMANDOS]
```

A partir de este punto, asumo que nos funciona brownie sin problema.

# Tutorial

En este tutorial utilizamos algo que se llama un brownie "mix". Esto es una serie de paquetes que nos permite importar contratos y arquitecturas mas complejas.

```bash
    # Creamos un repositorio de brownie conectado con react
    brownie bake react-mix app

    # Cambiamos a la carpeta de frontend (react)
    cd app/client
    
    # Instalamos dependencias del frontend
    npm install
```

Si quereis utilizar el contrato en una testnet recomiendo seguir con los pasos 4, 5 y 6 del [tutorial](https://github.com/brownie-mix/react-mix). Acordaos de utilizar una cuenta diferente a vuestra principal para no arriesgar fondos (por ejemplo, creando una nueva 'Account' en Metamask, o incluso desde brownie).

Debemos instalar [ganache-cli](https://github.com/trufflesuite/ganache), para permitir que brownie-eth pueda usar una red local. Tkinter es una libreria que nos permite crear una ventana que nos permita interactuar con la red local, pero rara vez la utilizo yo personalmente.

# Configurando el proyecto: Cartera Metamask
> Sin hacer estos cambios no va a funcionar la blockchain local.

Despues, podeis borrar en app/brownie-config.yaml la linea dotenv, y anadir vuestro account address. Por ejemplo yo uso `0x64B976BE4F56dbF10Ca31199eAF63DEc3002b883`, que es una cuenta extra, sin dinero real, en mi Metamask. 

Para crear cuentas en Metamask utiliza esta [guia](https://tinyurl.com/2p8fhfj6).

Ademas tenemos que asegurarnos de que nuestro metamask tiene fondos en la blockchain de prueba. Al crear una blockchain local con ganache-cli, nuestra cuenta de Metamask no tiene fondos necesariamente, asi que necesitamos cargarle fondos desde una de las carteras ya inicializadas. Dentro de app/scripts encontraremos `deploy.py`. 


En este script default tenemos:

```python
    # scripts/deploy.py
    from brownie import SolidityStorage, VyperStorage, accounts, network

    def main():
        # requires brownie account to have been created
        if network.show_active()=='development':
            # add these accounts to metamask by importing private key
            owner = accounts[0]
            SolidityStorage.deploy({'from':accounts[0]})
            VyperStorage.deploy({'from':accounts[0]})

        elif network.show_active() == 'kovan':
            # add these accounts to metamask by importing private key
            owner = accounts.load("main")
            SolidityStorage.deploy({'from':owner})
            VyperStorage.deploy({'from':owner})
```

Lo que tenemos que hacer es asegurarnos de que nuestra cuenta metamask tiene fondos.


# Publicando el contrato en la red local
Ahora vamos a crear una blockchain local con brownie, y a publicar los contratos inteligentes que vienen incluidos.

```bash
    brownie console

    # Dentro de la consola de brownie
    run('deploy')
```

Esto deberia crear una blockchain local con brownie, y a publicar los contratos inteligentes que podemos usar desde la web.

# Inicializar la aplicacion
Para comenzar la web vamos a app/client:

```bash
    cd app/client

    # Si usamos yarn
    yarn start

    # Si usamos npm
    npm start
```
Si queremos que utilice un navegador especifico, podemos usar por ejemplo 'BROWSER=chrome yarn start' o 'BROWSER=firefox yarn start'.

Ahora deberia abrirse una pagina web en la que aparece el valor que guarda cada uno de los contratos inteligentes. Podemos alterarlos desde la consola de brownie y desde la interfaz de la web.


    


