// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.6 <0.9.0;

import '@uniswap/v2-periphery/contracts/libraries/UniswapV2Library.sol';
import '@uniswap/v2-periphery/contracts/UniswapV2Router02.sol';
import '@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol';


contract UniswapExample {
    address public factory;
    constructor(address factory_) public {
        factory = factory_;

    }

    // function swap(address token1_, uint amountIn_) public {
    //     IUniswapV2Router02 router = IUniswapV2Router02(factory);
    //     IERC20 token1 = IERC20(token1_);

    //     require(token1.approve(address(router), uint(-1)), 'approve failed');

    //     uint256 amountIn = amountIn_;
    //     require(token1.transferFrom(msg.sender, address(this), amountIn), 'transferFrom failed.');

    //     address[] memory path = new address[](2);
    //     path[0] = address(token1);
    //     path[1] = router.WETH();
    //     uint256 amountOutMin = 1;
    //     router.swapExactTokensForETH(amountIn, amountOutMin, path, msg.sender, block.timestamp);
    //     msg.sender.transfer(address(this).balance);
    // }

    function pairInfo(address tokenA, address tokenB) internal view returns (uint reserveA, uint reserveB, uint totalSupply) {
        IUniswapV2Pair pair = IUniswapV2Pair(UniswapV2Library.pairFor(factory, tokenA, tokenB));
        totalSupply = pair.totalSupply();
        (uint reserves0, uint reserves1,) = pair.getReserves();
        (reserveA, reserveB) = tokenA == pair.token0() ? (reserves0, reserves1) : (reserves1, reserves0);
    }

    function swap(address token1_, address token2_, uint amountIn_) public {
        IUniswapV2Router02 router = IUniswapV2Router02(factory);
        IERC20 token1 = IERC20(token1_);
        IERC20 token2 = IERC20(token2_);

        uint256 amountIn = amountIn_;
        require(token1.transferFrom(msg.sender, address(this), amountIn), 'transferFrom failed.');

        require(token1.approve(address(router), uint(-1)), 'approve failed');

        address[] memory path = new address[](2);
        path[0] = address(token1);
        // path[1] = router.WETH();
        path[1] = address(token2);
        uint256 amountOutMin = 1;
        // router.swapExactTokensForETH(amountIn, amountOutMin, path, msg.sender, block.timestamp);
        // msg.sender.transfer(address(this).balance);
        router.swapExactTokensForTokens(
            amountIn,
            0, // amountOutMin: we can skip computing this number because the math is tested
            path,
            msg.sender,
            block.timestamp
        );
    }
}

// Token/Contract address: 0xA26de5AEC1C97d5EAc71f68c63B178CFbfd86B8c
// Token/Contract address: 0x5b23e6b8Fe58BDD00C7044BaB61C710748e04497
