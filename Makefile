setup-environment:
	npm init --yes
	npm install --save-dev hardhat
	npm install --save-dev @nomiclabs/hardhat-ethers ethers @nomiclabs/hardhat-waffle ethereum-waffle chai
	# yarn add hardhat --dev
	# yarn add @nomiclabs/hardhat-ethers ethers @nomiclabs/hardhat-waffle ethereum-waffle chai --dev

compile:
	npx hardhat compile

hardhat-node:
	npx hardhat node

deploy-hardhat-local:
	# npx hardhat run scripts/deploy.js # without --network will deploy to Hardhat network
	# npx hardhat run scripts/deploy.js --network localhost # same above
	npx hardhat run scripts/deploy.js --network local

deploy-rinkeby:
	npx hardhat run scripts/deploy.js --network rinkeby

deploy-ropsten:
	npx hardhat run scripts/deploy.js --network ropsten

deploy-avax-fuji:
	npx hardhat run scripts/deploy.js --network avalanche_fuji

flatten-all:
	rm -rf Output.sol
	npx hardhat flatten > Output.sol

flatten:
	rm -rf Output.sol
	# npx hardhat flatten contracts/token1.sol > Output.sol
	# npx hardhat flatten contracts/UniswapExample.sol > Output.sol
	npx hardhat flatten contracts/GodModeErc20.sol > Output.sol
