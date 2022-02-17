// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.6 <0.9.0;
import './token_common.sol';

//name this contract whatever you'd like
contract ERC20Token1 is StandardToken {

    fallback () external {
        //if ether is sent to this address, send it back.
        revert();
    }

    /* Public variables of the token */

    /*
    NOTE:
    The following variables are OPTIONAL vanities. One does not have to include them.
    They allow one to customise the token contract & in no way influences the core functionality.
    Some wallets/interfaces might not even bother to look at this information.
    */
    string public name;                   //fancy name: eg Simon Bucks
    uint8 public decimals;                //How many decimals to show. ie. There could 1000 base units with 3 decimals. Meaning 0.980 SBX = 980 base units. It's like comparing 1 wei to 1 ether.
    string public symbol;                 //An identifier: eg SBX
    string public version = 'H1.0';       //human 0.1 standard. Just an arbitrary versioning scheme.

//
// CHANGE THESE VALUES FOR YOUR TOKEN
//

//make sure this function name matches the contract name above. So if you're token is called TutorialToken, make sure the //contract name above is also TutorialToken instead of ERC20Token

    constructor () public {
        balances[tx.origin] = 100000;               // Give the creator all initial tokens (100000 for example)
        totalSupply = 100000;                        // Update total supply (100000 for example)
        name = "Xuan Anh test token 1";                                   // Set the name for display purposes
        decimals = 0;                            // Amount of decimals for display purposes
        symbol = "T1";                               // Set the symbol for display purposes
    }

    /* Approves and then calls the receiving contract */
    function approveAndCall(address _spender, uint256 _value, bytes memory _extraData) public returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);

        //call the receiveApproval function on the contract you want to be notified. This crafts the function signature manually so one doesn't have to include a contract in here just for this.
        //receiveApproval(address _from, uint256 _value, address _tokenContract, bytes _extraData)
        //it is assumed that when does this that the call *should* succeed, otherwise one would use vanilla approve instead.
        // if(!_spender.call(bytes4(bytes32(sha3("receiveApproval(address,uint256,address,bytes)"))), msg.sender, _value, this, _extraData)) { revert(); }
        return true;
    }
}

// rinkeby 0x37e68237F032Bafe198907Cd2D2365A7b82f801D
// ropsten 0xb1c39C8D4c284f7bfCb839fb551e0ee49c8Afb81