require("@nomiclabs/hardhat-waffle");
require('hardhat-ethernal');

/**
 * @type import('hardhat/config').HardhatUserConfig
 */

extendEnvironment((hre) => {
  hre.ethernalSync = true;
  hre.ethernalWorkspace = 'xuananh';
  // hre.ethernalTrace = false;   // default is true
  hre.ethernalResetOnStart = 'xuananh'; // ethernal workspace name
});

module.exports = {
  solidity: "0.6.6",
  networks: {
    local: {
      url: "http://localhost:8545", //Infura url with projectId
      accounts: ["ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"] // add the account that will deploy the contract (private key)
    },
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
