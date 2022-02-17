// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.6 <0.9.0;

// import '@uniswap/v2-periphery/contracts/libraries/UniswapV2Library.sol';
import '@uniswap/v2-periphery/contracts/UniswapV2Router02.sol';
import '@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol';

// import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";


contract UniswapExample {
    address public factory;
    constructor(address factory_) public {
        factory = factory_;
    }

    function swap(address token1_, uint amountIn_) public {
        IUniswapV2Router02 router = IUniswapV2Router02(factory);
        IERC20 token1 = IERC20(token1_);

        uint256 amountIn = amountIn_;
        // uint amountIn = amountIn_ * 10 ** token1.decimals();
        require(token1.transferFrom(msg.sender, address(this), amountIn), 'transferFrom failed.');

        require(token1.approve(address(router), amountIn), 'approve failed');

        address[] memory path = new address[](2);
        path[0] = address(token1);
        path[1] = router.WETH();
        uint256 amountOutMin = 1;
        router.swapExactTokensForETH(amountIn, amountOutMin, path, msg.sender, block.timestamp);
        // msg.sender.transfer(address(this).balance);
    }
}

// rinkeby 0x6e8093c82e167F1496E191c28Bd3c9ecEe87399C
// ropsten 0x6e8093c82e167F1496E191c28Bd3c9ecEe87399C
