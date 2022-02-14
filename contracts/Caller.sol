// SPDX-License-Identifier: GPL-3.0
// https://www.zupzup.org/smart-contract-interaction/
pragma solidity >=0.6.6 <0.9.0;

contract Caller {
    function someAction(address addr) public returns(uint) {
        ICallee c = ICallee(addr);
        return c.getValue(100);
    }
    
    function storeAction(address addr) public returns(uint) {
        ICallee c = ICallee(addr);
        c.storeValue(100);
        return c.getValues();
    }
    
    // function someUnsafeAction(address addr) public {
    //     addr.call(bytes4(keccak256("storeValue(uint256)")), 100);
    // }
}

interface ICallee {
    function getValue(uint initialValue) external returns(uint);
    function storeValue(uint value) external;
    function getValues() external returns(uint);
}

// Compiling 1 file with 0.7.3
// Solidity compilation finished successfully
// Deploying contracts with the account: 0xFFa2a2845924326045538DA9a72C40614001C561
// Account balance: 197669731831253394
// Token/Contract address: 0x517E15f123c86BF8051a40ef44995d49Ba9a8535
