// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// When running the script with `npx hardhat run <script>` you'll find the Hardhat
// Runtime Environment's members available in the global scope.

const hre = require("hardhat");
const ethers = hre.ethers;


async function main() {

  // Hardhat always runs the compile task when running scripts with its command
  // line interface.
  //
  // If this script is run directly using `node` you may want to call compile
  // manually to make sure everything is compiled
  // await hre.run('compile');

    const [deployer] = await ethers.getSigners();
  
    console.log("Deploying contracts with the account:", deployer.address);
    console.log("Account balance:", (await deployer.getBalance()).toString());
  
    // const ContractName = "SimpleToken";
    // const Token = await ethers.getContractFactory(ContractName);
    // const token = await Token.deploy();
    
    // await token.deployed()
    // await hre.ethernal.push({
    //   name: ContractName,
    //   address: token.address
    // })

    // const Token = await ethers.getContractFactory("XA1CoinERC20");
    // const token = await Token.deploy(100000);

    // const Token = await ethers.getContractFactory("XA2CoinERC20");
    // const token = await Token.deploy(100000);
    // console.log("XA2CoinERC20 address:", token.address);

    // const name = 'Coin 1';
    // const symbol = 'C1';

    // const name = 'Coin 2';
    // const symbol = 'C2';

    // const decimals = 18;
    // const Token = await ethers.getContractFactory("GodModeErc20");
    // const token = await Token.deploy(name, symbol, decimals);
    // console.log("GodModeErc20: address:", token.address);

    // const C2_ADDRESS = "0xc725f6243562C445b0352fc9Db99Ec17EB0Ad393"
    // const Token1 = await ethers.getContractFactory("TestContract");
    // const token1 = await Token1.deploy(C2_ADDRESS);
    // console.log("TestContract address:", token1.address);

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
