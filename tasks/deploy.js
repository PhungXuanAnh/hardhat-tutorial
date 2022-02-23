function test() {
    console.log("aaaaaaaaaaaaaaaaaaaaaa");
}

task("deploy", "Deploy a smart contract")
  .addParam("contractName", "contract name to deploy")
  .addOptionalParam("additionParams", "additional parameters to deploy", "nothing")
  .setAction(async (taskArgs, hre, runSuper) => {
    // console.log(taskArgs.contractName);
    // console.log(taskArgs.additionParams);
    const ethers = hre.ethers;
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);
    console.log("Account balance:", (await deployer.getBalance()).toString());

    var contractName = taskArgs.contractName;
    var contractConstructorArgs = taskArgs.additionParams.split(" ");
    console.log(contractConstructorArgs)
    const Contract = await ethers.getContractFactory(contractName);
    if (taskArgs.additionParams != undefined) {
        var contract = await Contract.deploy(...contractConstructorArgs);
    } else {
        var contract = await Contract.deploy();
    }
    
    console.log("Contract address:", contract.address);
    
    await contract.deployed()
    console.log("============ Deploy done ==========");

    await hre.ethernal.push({
      name: contractName,
      address: contract.address
    })
  });

module.exports = {}
