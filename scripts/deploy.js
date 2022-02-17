// const json = require('@uniswap/v2-core/build/UniswapV2Factory.json')
// const contract = require('@hardhat/contract');
// const UniswapV2Factory = contract(json);
const ethernal = require('hardhat-ethernal');
const hre = require("hardhat");
const { ethers } = require("hardhat");  // The ethers variable is available in the global scope. If you like your code always being explicit

async function main() {
    const [deployer] = await ethers.getSigners();
  
    console.log("Deploying contracts with the account:", deployer.address);
    console.log("Account balance:", (await deployer.getBalance()).toString());
  
    const ContractName = "SimpleToken";
    const Token = await ethers.getContractFactory(ContractName);
    const token = await Token.deploy();
    
    await token.deployed()
    await hre.ethernal.push({
      name: ContractName,
      address: token.address
    })
    // const Token = await ethers.getContractFactory("XA1CoinERC20");
    // const token = await Token.deploy(100000);

    // const Token = await ethers.getContractFactory("XA2CoinERC20");
    // const token = await Token.deploy(100000);

    // const Token1 = await ethers.getContractFactory("ERC20Token1");
    // const token1 = await Token1.deploy();
    // console.log("ERC20Token1 address:", token1.address);

    // const Token2 = await ethers.getContractFactory("ERC20Token2");
    // const token2 = await Token2.deploy();
    // console.log("ERC20Token2 address:", token2.address);

    // const Token = await ethers.getContractFactory("Callee");
    // const token = await Token.deploy();

    // const Token = await ethers.getContractFactory("Caller");
    // const token = await Token.deploy();

    // router = {}
    // factory = {}
    // // uniswap has the same address on mainnet and ropsten
    // router.address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D";
    // // factory.address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f";
    // const Token = await ethers.getContractFactory("UniswapExample");
    // const token = await Token.deploy(router.address);
    // console.log("UniswapExample address:", token.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
