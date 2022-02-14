compile:
	npx hardhat compile

start-hardhat-local-node:
	npx hardhat node

deploy-hardhat-localhost:
	# npx hardhat run scripts/deploy.js # without --network will deploy to Hardhat network
	npx hardhat run scripts/deploy.js --network localhost # same above

deploy-rinkeby:
	npx hardhat run scripts/deploy.js --network rinkeby

flatten-all:
	rm -rf Output.sol
	npx hardhat flatten > Output.sol

flatten:
	rm -rf Output.sol
	npx hardhat flatten contracts/UniswapExample.sol > Output.sol
