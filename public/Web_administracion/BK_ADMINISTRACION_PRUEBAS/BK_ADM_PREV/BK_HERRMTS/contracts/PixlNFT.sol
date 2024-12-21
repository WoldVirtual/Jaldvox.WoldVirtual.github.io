import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// This contract handles the creation and management of PixlNFT tokens.
contract PixlNFT is ERC721URIStorage { 

    using Counters for Counters.Counter; 
    Counters.Counter private _tokenIds;

    constructor() ERC721("ExampleNFT", "ENFT") {
    }

    function createToken(string memory tokenURI) public payable returns (uint) {
        // This function creates a new PixlNFT token with the given tokenURI.
        require(msg.value >= 1000000000000000000, "Not enough EHT sent; check price!");
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();

        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }
}
