require("@nomiclabs/hardhat-waffle");
require('hardhat-ethernal');
require("@nomiclabs/hardhat-web3");
require("./tasks")

task("balance", "Prints an account's balance")
  .addParam("account", "The account's address")
  .setAction(async (taskArgs) => {
    const account = web3.utils.toChecksumAddress(taskArgs.account);
    const balance = await web3.eth.getBalance(account);

    console.log(web3.utils.fromWei(balance, "ether"), "ETH");
    // to test this task run: npx hardhat balance --account 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
  });


/**
 * @type import('hardhat/config').HardhatUserConfig
 */

extendEnvironment((hre) => {
  // extend hardhat environment 
  // https://hardhat.org/advanced/hardhat-runtime-environment.html#extending-the-hre
  
  // extend ethernal function
  hre.ethernalSync = true;
  hre.ethernalWorkspace = 'xuananh';
  // hre.ethernalTrace = false;   // default is true
  hre.ethernalResetOnStart = 'xuananh'; // ethernal workspace name

  // extend Web3 
  // const Web3 = require("web3");
  // hre.Web3 = Web3;
  // // hre.network.provider is an EIP1193-compatible provider.
  // hre.web3 = new Web3(hre.network.provider);
});



module.exports = {

  // available config : https://hardhat.org/config/
  solidity: {
    // https://hardhat.org/guides/compile-contracts.html#multiple-solidity-versions
    // https://hardhat.org/guides/compile-contracts.html
    compilers: [ 
      {
        version: "0.6.6",
      },
      {
        version: "0.8.0",
        settings: {},
      },
    ],
  },
  defaultNetwork: "hardhat",
  networks: {
    // hardhat: {
    //   url: "http://localhost:8545", //Infura url with projectId
    //   accounts: ["ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"] // add the account that will deploy the contract (private key)
    // },
    rinkeby: {
      url: "https://rinkeby.infura.io/v3/209b0f36b12b4e50951ce0f0d5b241e3", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
    avalanche_fuji: {
      url: "https://api.avax-test.network/ext/bc/C/rpc", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
    ropsten: {
      url: "https://ropsten.infura.io/v3/209b0f36b12b4e50951ce0f0d5b241e3", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
  }
};
