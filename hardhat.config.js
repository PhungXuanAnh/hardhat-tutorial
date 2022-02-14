require("@nomiclabs/hardhat-waffle");

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.6.6",
  networks: {
    rinkeby: {
      url: "https://rinkeby.infura.io/v3/209b0f36b12b4e50951ce0f0d5b241e3", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
    avax: {
      url: "https://api.avax-test.network/ext/bc/C/rpc", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
    local: {
      url: "http://localhost:8545", //Infura url with projectId
      accounts: ["5dc0c12f82b98c275040b5c3526514603f0df98b9ef27317cb5e51807c1fd79c"] // add the account that will deploy the contract (private key)
    },
  }
};
