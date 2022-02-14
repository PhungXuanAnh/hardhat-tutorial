- [1. prepare environment](#1-prepare-environment)
- [2. compiling](#2-compiling)
- [3. run test](#3-run-test)
- [4. deploy](#4-deploy)
- [flatten contract](#flatten-contract)
- [5. faucet](#5-faucet)
  - [5.1. rinkeby](#51-rinkeby)
- [6. ---](#6----)

# 1. prepare environment

```shell
mkdir hardhat-tutorial
cd hardhat-tutorial
npm init --yes
npm install --save-dev hardhat
mkdir hardhat-tutorial
# Select Create an empty hardhat.config.js with your keyboard and hit enter.
npm install --save-dev @nomiclabs/hardhat-ethers ethers @nomiclabs/hardhat-waffle ethereum-waffle chai
```

# 2. compiling

```shell
npx hardhat compile
```

# 3. run test

```shell
npx hardhat test
```

# 4. deploy

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

# flatten contract

https://github.com/nomiclabs/hardhat/issues/1049#issuecomment-1022809292

```shell
cd hardhat-tutorial
npx hardhat flatten > Output.sol
# or
npx hardhat flatten contracts/UniswapExample.sol > Output.sol
```

# 5. faucet

## 5.1. rinkeby

https://faucets.chain.link/rinkeby

# 6. ---

```shell
npm install @openzeppelin/contracts
```
