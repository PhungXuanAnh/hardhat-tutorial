- [1. local development](#1-local-development)
  - [1.1. prepare environment](#11-prepare-environment)
  - [1.2. compiling](#12-compiling)
  - [1.3. run test](#13-run-test)
  - [1.4. deploy](#14-deploy)
  - [1.5. flatten contract](#15-flatten-contract)
- [2. faucet](#2-faucet)
  - [2.1. rinkeby](#21-rinkeby)
- [3. other](#3-other)
  - [3.1. LIFE](#31-life)
  - [3.2. uniswap liquidity](#32-uniswap-liquidity)
  - [3.3. swap steps](#33-swap-steps)
  - [3.4. liquidity explain](#34-liquidity-explain)

# 1. local development
## 1.1. prepare environment

```shell
mkdir hardhat-tutorial
cd hardhat-tutorial
npm init --yes
npm install --save-dev hardhat
mkdir hardhat-tutorial
# Select Create an empty hardhat.config.js with your keyboard and hit enter.
npm install --save-dev @nomiclabs/hardhat-ethers ethers @nomiclabs/hardhat-waffle ethereum-waffle chai
```

## 1.2. compiling

```shell
npx hardhat compile
```

## 1.3. run test

```shell
npx hardhat test
```

## 1.4. deploy

```shell
npx hardhat run scripts/deploy.js --network <network-name>
# 3. example
npx hardhat run scripts/deploy.js # without --network will deploy to Hardhat network
# 4. output
Deploying contracts with the account: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
Account balance: 10000000000000000000000
Token address: 0x5FbDB2315678afecb367f032d93F642f64180aa3

# 5. or
npx hardhat run scripts/deploy.js --network rinkeby
```

## 1.5. flatten contract

https://github.com/nomiclabs/hardhat/issues/1049#issuecomment-1022809292

```shell
cd hardhat-tutorial
npx hardhat flatten > Output.sol
# or
npx hardhat flatten contracts/UniswapExample.sol > Output.sol
```

# 2. faucet

## 2.1. rinkeby

https://faucets.chain.link/rinkeby

# 3. other

```shell
npm install @openzeppelin/contracts
```

## 3.1. LIFE
https://testnet.snowtrace.io/token/0x19984415D191514fC50aE7dc44fbd885EABb00AF

all address on avax fuji

```shell
 Network: avax-fuji
=> gfn_deployer: 0xD26132ffC40B3A24ab7b45741c7518610CFdc9d4
=> gfn_owner: 0xD26132ffC40B3A24ab7b45741c7518610CFdc9d4
=> ContractRegistry Address: 0x33D4F6a08D253fc7fAaBa0050Fa4abcA9a612c4F
=> GNFTToken Address: 0x26bB536177F22739e0255700091eE72145C96aaF
=> LIFEToken Address: 0x19984415D191514fC50aE7dc44fbd885EABb00AF
=> LIFETreasury Address: 0xeC22c14877480d2a9e6878363aC2A24aA1692331
```

## 3.2. uniswap liquidity

10 LIFE = 1     XA1C
10 LIFE = 1.02  XA1C

## 3.3. swap steps

choose from/to token
click Approved

## 3.4. liquidity explain

Hải Lương Quang3:58 PM
x * y = k
100 LIFE  | USDT 1000
=> k = 100 000
Hải Lương Quang4:00 PM
5 LIFE
-> 105 LIFE
Hải Lương Quang4:01 PM
100 000 / 105 = 952 USDT
1000 - 952 = 48 USDT
Hải Lương Quang4:04 PM
1200 | 400 => k = 480 000
x = 1203.03
y = 3.99
Hải Lương Quang4:05 PM
y = 399
400 - 399 = 1
