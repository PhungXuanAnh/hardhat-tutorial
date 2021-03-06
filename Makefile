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
	# npx hardhat flatten contracts/TestContract.sol > Output.sol

deploy-XA1CoinERC20:
	npx hardhat deploy --contract-name XA1CoinERC20 --addition-params 100000

deploy-GodModeErc20-C1:
	npx hardhat deploy --contract-name GodModeErc20 --addition-params "Coin1 C1 18"

deploy-GodModeErc20-C2:
	npx hardhat deploy --contract-name GodModeErc20 --addition-params "Coin2 C2 18"

deploy-GodModeErc20-USDT-fuji:	# 0x6e8093c82e167F1496E191c28Bd3c9ecEe87399C
	npx hardhat deploy --network avalanche_fuji \
		--contract-name GodModeErc20 \
		--addition-params "xuananh-USDT USDT 18"

deploy-GodModeErc20-LIFE-fuji: # 0x721d9B2E7C14fE892B712E09d926719e023BFCaE
	npx hardhat deploy --network avalanche_fuji \
		--contract-name GodModeErc20 \
		--addition-params "xuananh-LIFE LIFE 18"
		