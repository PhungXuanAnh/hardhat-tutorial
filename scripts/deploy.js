// const json = require('@uniswap/v2-core/build/UniswapV2Factory.json')
// const contract = require('@hardhat/contract');
// const UniswapV2Factory = contract(json);


async function main() {
    const [deployer] = await ethers.getSigners();
  
    console.log("Deploying contracts with the account:", deployer.address);
  
    console.log("Account balance:", (await deployer.getBalance()).toString());
  
    // const Token = await ethers.getContractFactory("Token");
    // const token = await Token.deploy();

    // const Token = await ethers.getContractFactory("XA1CoinERC20");
    // const token = await Token.deploy(100000);

    // const Token = await ethers.getContractFactory("XA2CoinERC20");
    // const token = await Token.deploy(100000);

    // const Token = await ethers.getContractFactory("UniswapV2Factory");
    const Token = await ethers.getContractFactoryFromArtifact("UniswapV2Factory");
    const token = await Token.deploy();

    // const Token = await ethers.getContractFactory("Callee");
    // const token = await Token.deploy();

    // const Token = await ethers.getContractFactory("Caller");
    // const token = await Token.deploy();

    // const Token = await ethers.getContractFactory("UniswapExample");
    // const token = await Token.deploy("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D");
  
    console.log("Token/Contract address:", token.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
