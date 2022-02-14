// SPDX-License-Identifier: GPL-3.0
// https://www.zupzup.org/smart-contract-interaction/
pragma solidity >=0.6.6 <0.9.0;

contract Callee {
    uint[] public values;

    function getValue(uint initial) public pure returns(uint) {
        return initial + 150;
    }
    function storeValue(uint value) public {
        values.push(value);
    }
    function getValues() public view returns(uint) {
        return values.length;
    }
}

// Compiling 1 file with 0.7.3
// Solidity compilation finished successfully
// Deploying contracts with the account: 0xFFa2a2845924326045538DA9a72C40614001C561
// Account balance: 197893734332597409
// Token address: 0x51dCC77071A2996EF73c50997C80003a3D2c1cC8

